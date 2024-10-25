# Порівняння алгоритмів сортування: Merge Sort, Insertion Sort, Timsort

## Огляд
У цьому дослідженні порівнюються три алгоритми сортування: **злиттям** (Merge Sort), **вставками** (Insertion Sort) та **Timsort** (вбудований в Python). Ми оцінювали продуктивність алгоритмів за допомогою емпіричних даних, отриманих під час тестування на різних наборах даних.

## Результати та висновки

### 1. Алгоритм сортування злиттям (Merge Sort)
- **Складність:** 
  - Найгірша, середня та найкраща складності: `O(n log n)`.
- **Переваги:** 
  - Підходить для великих масивів, оскільки має стабільну продуктивність.
  - Стабільний алгоритм, зберігає порядок елементів з однаковими значеннями.
- **Недоліки:** 
  - Використовує додаткову пам'ять для об'єднання частин масиву.
- **Емпіричні результати:** 
  - На малих і середніх масивах працює повільніше, ніж Timsort, але швидше за сортування вставками.
  - Продуктивність стабільна на великих масивах.

### 2. Алгоритм сортування вставками (Insertion Sort)
- **Складність:** 
  - Найгірша і середня складності: `O(n^2)`.
  - Найкраща складність для майже відсортованих масивів: `O(n)`.
- **Переваги:** 
  - Ефективний для малих масивів або для майже відсортованих масивів.
  - Простий у реалізації, не потребує додаткової пам'яті.
- **Недоліки:** 
  - Повільний на великих масивах через квадратичну складність.
- **Емпіричні результати:** 
  - Швидкий на малих масивах, але не підходить для середніх і великих масивів.

### 3. Алгоритм Timsort (вбудований у Python)
- **Складність:** 
  - Найгірша та середня складності: `O(n log n)`.
  - Найкраща складність: `O(n)`.
- **Переваги:** 
  - Поєднує сортування злиттям і вставками, що робить його ефективним для частково відсортованих масивів.
  - Стабільний алгоритм, оптимізований для роботи з реальними даними.
- **Недоліки:** 
  - Складніший у реалізації порівняно з іншими алгоритмами.
- **Емпіричні результати:** 
  - Показав найкращі результати для всіх розмірів масивів, особливо на великих масивах.
  - Завдяки комбінації алгоритмів, має найкращу продуктивність у більшості випадків.

## Загальні висновки
- **Timsort** є найефективнішим алгоритмом, особливо на великих наборах даних, оскільки поєднує переваги сортування злиттям і вставками.
- **Сортування злиттям** залишається ефективним вибором для великих масивів, але поступається Timsort у продуктивності на частково відсортованих даних.
- **Сортування вставками** є найбільш ефективним для малих масивів або масивів, які вже майже відсортовані, але втрачає ефективність на великих наборах даних.

Timsort є гібридним алгоритмом, який поєднує кращі характеристики обох методів сортування, і саме тому він використовується як вбудований алгоритм сортування в Python.
