def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        sol = arr[:mid]
        sag = arr[mid:]

        # Alt dizileri sıralamak için rekürsif çağrı
        merge_sort(sol)
        merge_sort(sag)

        i = j = k = 0
        # İki alt diziyi birleştir
        while i < len(sol) and j < len(sag):
            if sol[i] < sag[j]:
                arr[k] = sol[i]
                i += 1
            else:
                arr[k] = sag[j]
                j += 1
            k += 1

        # Sol kalan elemanları ekle
        while i < len(sol):
            arr[k] = sol[i]
            i += 1
            k += 1

        # Sağ kalan elemanları ekle
        while j < len(sag):
            arr[k] = sag[j]
            j += 1
            k += 1

# Örnek kullanım
liste = [38, 27, 43, 3, 9, 82, 10]
print("Sıralanmadan önce:", liste)
merge_sort(liste)
print("Sıralandıktan sonra:", liste)
