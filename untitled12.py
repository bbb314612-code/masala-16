# Array36: Lokal minimum yoki lokal maksimum bo'lmagan elementlar ichida eng kattasini topish.
# Agar bunday element bo'lmasa, 0 qaytariladi.
def array36(arr):
    n = len(arr)
    max_val = None
    
    for i in range(n):
        # Chekka elementlar uchun qo'shnilarini tekshirish sharti
        is_local_min = True
        is_local_max = True
        
        # Chap qo'shni tekshiruvi
        if i > 0:
            if arr[i] >= arr[i-1]: is_local_min = False
            if arr[i] <= arr[i-1]: is_local_max = False
            
        # O'ng qo'shni tekshiruvi
        if i < n - 1:
            if arr[i] >= arr[i+1]: is_local_min = False
            if arr[i] <= arr[i+1]: is_local_max = False
            
        # Agar element lokal minimum ham, lokal maksimum ham bo'lmasa
        if not is_local_min and not is_local_max:
            if max_val == None or arr[i] > max_val:
                max_val = arr[i]
                
    return max_val if max_val is not None else 0


# Array37: Monoton o'suvchi oraliqlar (bo'laklar) sonini aniqlash.
def array37(arr):
    n = len(arr)
    if n == 0: return 0
    
    count = 0
    in_interval = False
    
    for i in range(n - 1):
        if arr[i] < arr[i+1]:
            if not in_interval:
                count += 1
                in_interval = True
        else:
            in_interval = False
            
    return count


# Array38: Monoton kamayuvchi oraliqlar (bo'laklar) sonini aniqlash.
def array38(arr):
    n = len(arr)
    if n == 0: return 0
    
    count = 0
    in_interval = False
    
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            if not in_interval:
                count += 1
                in_interval = True
        else:
            in_interval = False
            
    return count


# Array39: Monoton (yoki faqat o'suvchi, yoki faqat kamayuvchi) oraliqlar umumiy soni.
def array39(arr):
    # Array37 va Array38 natijalarining yig'indisi monoton oraliqlar sonini beradi
    return array37(arr) + array38(arr)


# Array40: Massiv elementlari ichidan R soniga eng yaqin qiymatni topish.
# Ya'ni |a[k] - R| ayirmasi eng kichik bo'lgan a[k] topiladi.
def array40(arr, R):
    if not arr: return None
    
    closest_element = arr[0]
    min_diff = abs(arr[0] - R)
    
    for x in arr:
        diff = abs(x - R)
        if diff < min_diff:
            min_diff = diff
            closest_element = x
            
    return closest_element


# === DASTURNI TEKSHIRISH (NAMUNA) ===
if __name__ == "__main__":
    # Test uchun massivlar
    test_arr1 = [1, 5, 3, 4, 8, 2, 6]
    test_arr2 = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1] # O'suvchi va kamayuvchi qismlari bor
    
    print("--- Array36 Natijasi ---")
    print(f"Massiv: {test_arr1}")
    print(f"Lokal Ekstremum bo'lmagan eng katta element: {array36(test_arr1)}")
    print()

    print("--- Array37 va Array38 Natijalari ---")
    print(f"Massiv: {test_arr2}")
    print(f"Monoton o'suvchi oraliqlar soni: {array37(test_arr2)}")
    print(f"Monoton kamayuvchi oraliqlar soni: {array38(test_arr2)}")
    print()

    print("--- Array39 Natijasi ---")
    print(f"Umumiy monoton oraliqlar soni: {array39(test_arr2)}")
    print()

    print("--- Array40 Natijasi ---")
    R_soni = 11
    test_arr3 = [2, 5, 8, 15, 23]
    print(f"Massiv: {test_arr3}, R = {R_soni}")
    print(f"R soniga eng yaqin element: {array40(test_arr3, R_soni)}")
