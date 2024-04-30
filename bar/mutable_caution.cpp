#include <iostream>

#include "bar/bar.pb.h"

int main() {
    bar::Bar bar;
    bar.set_y(456);

    std::cout << "Before mutable_foo(): &foo = " << &bar.foo()
            << ", bar =\n" << bar.DebugString() << '\n';

    auto* foo = bar.mutable_foo();
    std::cout << "After mutable_foo(): &foo = " << &bar.foo()
            << ", bar =\n" << bar.DebugString() << '\n';

    foo->set_x(123);
    std::cout << "After set_x(): &foo = " << &bar.foo()
            << ", bar =\n" << bar.DebugString() << '\n';
    return 0;
}
