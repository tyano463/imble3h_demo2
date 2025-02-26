CC 		:= 	/opt/microchip/xc8/v3.00/bin/xc8-cc
CFLAGS 	:= -mcpu=18F26Q84
LDFLAGS	:= -mcpu=18F26Q84
OBJS	:= $(patsubst %.c, %.p1, $(wildcard *.c))
EXE		:= demo2.hex

all: $(OBJS)
	$(CC) $(LDFLAGS) $^ -o $(EXE)

%.p1: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(EXE) startup.* *.sym *.cmf *.hxl *.elf *.sdb *.d *.o *.S *.s
