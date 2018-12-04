#include "../../../io.h"
#include <string.h>


int main(int argc, char* argv[]) {
    char* input = read_file("input.txt");

    char* token;
    int calc = 0;
    
    while ((token = strsep(&input, "\n")))
        calc += atoi(token);

    free(input);
    free(token);

    printf("%d\n", calc);
    return 0;
}
