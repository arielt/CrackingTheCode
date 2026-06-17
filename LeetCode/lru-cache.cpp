// https://leetcode.com/problems/lru-cache/

#include <list>
#include <map>

using namespace std;

class LRUCache {
private:
    int capacity;
    list<int> dll;
    unordered_map<int, pair<list<int>::iterator, int>> map;

    void move_to_first_(int key) {
        dll.erase(map[key].first);
        dll.push_front(key);
        map[key].first = dll.begin();
    }

public:
    LRUCache(int capacity) : capacity(capacity) {
    }
    
    int get(int key) {
        if (!map.contains(key)) {
            return -1;
        }

        move_to_first_(key);
        return map[key].second;
    }
    
    void put(int key, int value) {
        if (map.contains(key)) {
            map[key].second = value;
            move_to_first_(key);
        } else {
            dll.push_front(key);
            map[key] = {dll.begin(), value};
            capacity--;
        }

        if (capacity < 0) {
            map.erase(dll.back());
            dll.pop_back();
            capacity++;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */