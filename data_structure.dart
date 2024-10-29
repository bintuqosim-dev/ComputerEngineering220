import 'package:collection/collection.dart';

List<int> maxSlidingWindow(List<int> arr, int k) {
  List<int> ans = [];
  PriorityQueue<MapEntry<int, int>> maxHeap =
      PriorityQueue<MapEntry<int, int>>((a, b) => b.key.compareTo(a.key));

  for (int i = 0; i < k; i++) {
    maxHeap.add(MapEntry(arr[i], i));
  }
  ans.add(maxHeap.first.key);

  for (int i = k; i < arr.length; i++) {
    maxHeap.add(MapEntry(arr[i], i));

    while (maxHeap.first.value <= i - k) {
      maxHeap.removeFirst();
    }

    ans.add(maxHeap.first.key);
  }

  return ans;
}

void main() {
  List<int> arr = [2, 3, 7, 9, 5, 1, 6, 4, 3];
  int k = 3;
  List<int> res = maxSlidingWindow(arr, k);
  for (int value in res) {
    print(value);
  }
}
