#include <iostream>
#include <string.h>
#include <stdio.h>

extern "C"
{
    void* int2str(int i)
    {
        std::string str = std::to_string(i);
        std::cout << "str: " << str << "\n";
        char *res = strdup( str.c_str() );
        printf("Address of new string is %p\n", res);
        return res;
    }

    void free_memory(void *ptr)
    {
        printf("Address of free memory: %p\n", ptr);
        free(ptr);
    }

    int fibonacci(int n)
    {
        if (n < 2)
            return 1;
        return fibonacci(n-2) + fibonacci(n-1);
    }
}
