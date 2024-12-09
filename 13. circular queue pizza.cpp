#include <iostream>
using namespace std;
#define size 5
class pizza {
    int porder[size];
    int front, rear;
    int count = 0;
public:
    pizza() {
        front = rear = -1;
    }
    int qfull() {
        if ((front == 0 && rear == (size - 1)) || (front == (rear + 1) % size))
            return 1;
        else
            return 0;
    }
    int qempty() {
        if (front == -1)
            return 1;
        else
            return 0;
    }
    void accept_order(int);
    void make_payment(int);
    void order_in_queue();};
void pizza::accept_order(int item) {
    if (qfull())
        cout << "\nVery Sorry !!!! No more orders....\n";
    else {
        if (front == -1) {
            front = rear = 0;
        } else {
            rear = (rear + 1) % size;
        }
        porder[rear] = item;
        count++;
    } }
void pizza::make_payment(int n) {
    int item;
    if (qempty())
        cout << "\nSorry !!! order is not there...\n";
    else if (n > count){
        cout << "\nSorry !!! You are trying to pay for more pizzas than available...\n";
        cout<<"there are only"<<" "<<count<<"pizza!"<<endl;}
    else {
        cout << "\nDelivered orders as follows...\n";
        for (int i = 0; i < n; i++) {
            item = porder[front];
            if (front == rear) {
                front = rear = -1;
            } else {
                front = (front + 1) % size;
            }
            cout << "\t" << item; }
        count -= n;
        cout << "\nTotal amount to pay : " << n * 100;
        cout << "\nThank you, visit again....\n";
    }
}
void pizza::order_in_queue() {
    int temp;
    if (qempty()) {
        cout << "\nSorry !! There is no pending order...\n";
    } else {
        temp = front;
        cout << "\nPending Order as follows..\n";
        while (temp != rear) {
            cout << "\t" << porder[temp];
            temp = (temp + 1) % size;
        }
        cout << "\t" << porder[temp];
    }
}
int main() {
    pizza p1;
    int ch, k, n;
    do {
        cout << "\n\t***** Welcome To Pizza Parlor *******\n";
        cout << "\n1. Accept order\n2. Make payment\n3. Pending Orders\nEnter your choice: ";
        cin >> ch;
        switch (ch) {
            case 1:
                cout << "\nWhich Pizza do you like most....\n";
                cout << "\n1. Veg Soya Pizza\n2. Veg Butter Pizza\n3. Egg Pizza";
                cout << "\nPlease enter your order: ";
                cin >> k;
                p1.accept_order(k);
                break;
            case 2:
                cout << "\nHow many Pizzas? ";
                cin >> n;
                p1.make_payment(n);
                break;
            case 3:
                cout << "\nFollowing orders are in queue to deliver....as follows..\n";
                p1.order_in_queue();
                break;
        }
    } while (ch != 4);
    return 0;
}

