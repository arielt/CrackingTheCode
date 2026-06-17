// https://leetcode.com/problems/print-in-order/

// mutex

using namespace std;

class Foo {
private:
    mutex first_mutex_;
    mutex second_mutex_;

public:
    Foo() {
        first_mutex_.lock();
        second_mutex_.lock();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        first_mutex_.unlock();
    }

    void second(function<void()> printSecond) {
        first_mutex_.lock();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        second_mutex_.unlock();
    }

    void third(function<void()> printThird) {
        second_mutex_.lock();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};

// condition variable
using namespace std;

class Foo {
private:
    mutex mtx;
    condition_variable cv;
    int count{};

public:
    Foo() {
        count = 1;
    }

    void first(function<void()> printFirst) {
        unique_lock<mutex> lck(mtx);
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        count = 2;
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lck(mtx);
        cv.wait(lck, [this]{return count == 2;});

        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        count = 3;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lck(mtx);
        cv.wait(lck, [this]{return count == 3;});

        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};

// semaphore
#include <semaphore>

using namespace std;

class Foo {
private:
    binary_semaphore sem1{0};
    binary_semaphore sem2{0};

public:
    Foo() {
        
    }

    void first(function<void()> printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        sem1.release();
    }

    void second(function<void()> printSecond) {
        sem1.acquire();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        sem2.release();
    }

    void third(function<void()> printThird) {
        sem2.acquire();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};
