import ray
import socket
import tensorflow as tf  # TensorFlow'u buraya dahil edin

# Ray'i başlat
ray.init() 

# GPU görevini tanımla
@ray.remote(num_gpus=1)
def gpu_task(x):
    return x * x  # Örnek GPU görevi

# Düğümler arası mesaj gönderme
def send_task_to_node(task_data, node_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((node_ip, 9000))  # libp2p düğümüne bağlan
    s.sendall(task_data.encode('utf-8'))
    result = s.recv(1024)
    s.close()
    return result.decode('utf-8')  # Sonucu geri döndür

# Görev sonuçlarını toplama fonksiyonu
def collect_results():
    results = []
    for node in ['localhost']:  # Aynı makinede çalışıyorsanız 'localhost' kullanabilirsiniz
        result = send_task_to_node("compute_task", node)
        results.append(result)  # Sonucu listeye ekle
    return results

# GPU görevlerini başlat ve sonuçları al
futures = [gpu_task.remote(i) for i in range(5)]  # GPU görevlerini başlat
results = ray.get(futures)  # Sonuçları al
print("GPU sonuçları:", results)

# P2P ağı üzerinden düğüm sonuçlarını topla
print("Toplanan Sonuçlar:", collect_results())