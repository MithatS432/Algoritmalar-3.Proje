def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # key'den büyük elemanları bir sağa kaydır
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # key'i doğru pozisyona yerleştir
        arr[j + 1] = key

# Örnek kullanım
liste = [12, 11, 13, 5, 6]
print("Sıralanmadan önce:", liste)
insertion_sort(liste)
print("Sıralandıktan sonra:", liste)
