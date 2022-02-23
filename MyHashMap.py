
class MyHashMap:
    def __init__(self):
        self.arr = [[] for i in range(10000)]

    def put(self, key, value):
        bucket_idx = self.get_bucket_idx(key)
        link_list = self.arr[bucket_idx]
        is_existed = False
        for tuple in link_list:
            old_key, old_value = tuple[0], tuple[1]
            if key == old_key:
                tuple[1] = value
                is_existed = True
                break
        if not is_existed:
            link_list.append((key, value))

    def get(self, key):
        bucket_idx = self.get_bucket_idx(key)
        link_list = self.arr[bucket_idx]
        for tuple in link_list:
            old_key, old_value = tuple[0], tuple[1]
            if key == old_key:
                return old_value
        return None

    def remove(self, key):
        bucket_idx = self.get_bucket_idx(key)
        link_list = self.arr[bucket_idx]
        key_idx = -1
        for i, tuple in enumerate(link_list):
            if tuple[0] == key:
                key_idx = i
        if key_idx != -1:
            new_arr = link_list[:key_idx].extend(link_list[key_idx + 1:])
            if not new_arr:
                new_arr = []
            self.arr[bucket_idx] = new_arr

    def get_bucket_idx(self, key):
        bucket_idx = key % len(self.arr)
        return bucket_idx




if __name__ == '__main__':
    myhashmap = MyHashMap()
    myhashmap.put(1, 1)
    ans1 = myhashmap.get(1)

    myhashmap.put(10001, 10001)
    ans2 = myhashmap.get(10001)
    print(ans1)
    print(ans2)
    myhashmap.remove(10001)
    ans3 = myhashmap.get(10001)
    print(ans3)