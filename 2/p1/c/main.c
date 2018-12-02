#include "../../../io.h"
#include <string.h>


int count_char(char* identifier, char c) {
    int count = 0;

    for (int i = 0; i < strlen(identifier); i++)
        if (identifier[i] == c)
            count++;

    return count;
}

int assert_count_char(char* identifier, int n) {
    for (int i = 0; i < strlen(identifier); i++)
        if (count_char(identifier, identifier[i]) == n)
            return 1;

    return 0;
}

int main(int argc, char* argv[]) {
    char* input = read_file("input.txt");

    char* token;
    int calc_2 = 0;
    int calc_3 = 0;
    while ((token = strsep(&input, "\n"))) {
        if (assert_count_char(token, 2))
            calc_2++;
        if (assert_count_char(token, 3))
            calc_3++;
    }

    free(input);
    free(token);

    printf("%d\n", calc_2 * calc_3);
    return 0;
}
