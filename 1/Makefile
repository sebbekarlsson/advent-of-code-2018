OS := $(shell uname)

$(info $(OS))

G_FLAGZ= -Wall -g

EXEC = a.out
SOURCES := $(wildcard *.c ../*.c)
OBJECTS = $(SOURCES:.c=.o)


$(EXEC): $(OBJECTS)
	gcc $(OBJECTS) $(FLAGZ) -o $(EXEC)

%.o: %.c %.h
	gcc -c $(G_FLAGZ) $< -o $@

clean:
	-rm *.out
	-rm *.o
