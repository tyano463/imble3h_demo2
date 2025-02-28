// CONFIG1
#pragma config FEXTOSC = OFF           // External Oscillator Selection (Oscillator not enabled)
#pragma config RSTOSC = HFINTOSC_64MHZ // Reset Oscillator Selection (HFINTOSC with HFFRQ = 64 MHz and CDIV = 1:1)

// CONFIG2
#pragma config CLKOUTEN = OFF // Clock out Enable bit (CLKOUT function is disabled)
#pragma config PR1WAY = OFF   // PRLOCKED One-Way Set Enable bit (PRLOCKED bit can be set and cleared repeatedly)
#pragma config CSWEN = ON     // Clock Switch Enable bit (Writing to NOSC and NDIV is allowed)
#pragma config JTAGEN = ON    // JTAG Enable bit (Enable JTAG Boundary Scan mode and pins)
#pragma config FCMEN = ON     // Fail-Safe Clock Monitor Enable bit (Fail-Safe Clock Monitor enabled)
#pragma config FCMENP = ON    // Fail-Safe Clock Monitor -Primary XTAL Enable bit (FSCM timer will set FSCMP bit and OSFIF interrupt on Primary XTAL failure)
#pragma config FCMENS = ON    // Fail-Safe Clock Monitor -Secondary XTAL Enable bit (FSCM timer will set FSCMS bit and OSFIF interrupt on Secondary XTAL failure)

// CONFIG3
#pragma config MCLRE = EXTMCLR  // MCLR Enable bit (If LVP = 0, MCLR pin is MCLR; If LVP = 1, RE3 pin function is MCLR )
#pragma config PWRTS = PWRT_OFF // Power-up timer selection bits (PWRT is disabled)
#pragma config MVECEN = ON      // Multi-vector enable bit (Multi-vector enabled, Vector table used for interrupts)
#pragma config IVT1WAY = ON     // IVTLOCK bit One-way set enable bit (IVTLOCKED bit can be cleared and set only once)
#pragma config LPBOREN = OFF    // Low Power BOR Enable bit (Low-Power BOR disabled)
#pragma config BOREN = SBORDIS  // Brown-out Reset Enable bits (Brown-out Reset enabled , SBOREN bit is ignored)

// CONFIG4
#pragma config BORV = VBOR_1P9 // Brown-out Reset Voltage Selection bits (Brown-out Reset Voltage (VBOR) set to 1.9V)
#pragma config ZCD = OFF       // ZCD Disable bit (ZCD module is disabled. ZCD can be enabled by setting the ZCDSEN bit of ZCDCON)
#pragma config PPS1WAY = ON    // PPSLOCK bit One-Way Set Enable bit (PPSLOCKED bit can be cleared and set only once; PPS registers remain locked after one clear/set cycle)
#pragma config STVREN = ON     // Stack Full/Underflow Reset Enable bit (Stack full/underflow will cause Reset)
#pragma config LVP = ON        // Low Voltage Programming Enable bit (Low voltage programming enabled. MCLR/VPP pin function is MCLR. MCLRE configuration bit is ignored)
#pragma config XINST = OFF     // Extended Instruction Set Enable bit (Extended Instruction Set and Indexed Addressing Mode disabled)

// CONFIG5
#pragma config WDTCPS = WDTCPS_31 // WDT Period selection bits (Divider ratio 1:65536; software control of WDTPS)
#pragma config WDTE = OFF         // WDT operating mode (WDT Disabled; SWDTEN is ignored)

// CONFIG6
#pragma config WDTCWS = WDTCWS_7 // WDT Window Select bits (window always open (100%); software control; keyed access not required)
#pragma config WDTCCS = SC       // WDT input clock selector (Software Control)

// CONFIG7
#pragma config BBSIZE = BBSIZE_512 // Boot Block Size selection bits (Boot Block size is 512 words)
#pragma config BBEN = OFF          // Boot Block enable bit (Boot block disabled)
#pragma config SAFEN = OFF         // Storage Area Flash enable bit (SAF disabled)
#pragma config DEBUG = ON          // Background Debugger (Background Debugger enableed)

// CONFIG8
#pragma config WRTB = OFF   // Boot Block Write Protection bit (Boot Block not Write protected)
#pragma config WRTC = OFF   // Configuration Register Write Protection bit (Configuration registers not Write protected)
#pragma config WRTD = OFF   // Data EEPROM Write Protection bit (Data EEPROM not Write protected)
#pragma config WRTSAF = OFF // SAF Write protection bit (SAF not Write Protected)
#pragma config WRTAPP = OFF // Application Block write protection bit (Application Block not write protected)

// CONFIG9
#pragma config BOOTPINSEL = RC5 // CRC on boot output pin selection (CRC on boot output pin is RC5)
#pragma config BPEN = OFF       // CRC on boot output pin enable bit (CRC on boot output pin disabled)
#pragma config ODCON = OFF      // CRC on boot output pin open drain bit (Pin drives both high-going and low-going signals)

// CONFIG10
#pragma config CP = OFF // PFM and Data EEPROM Code Protection bit (PFM and Data EEPROM code protection disabled)

// CONFIG11
#pragma config BOOTSCEN = OFF // CRC on boot scan enable for boot area (CRC on boot will not include the boot area of program memory in its calculation)
#pragma config BOOTCOE = HALT // CRC on boot Continue on Error for boot areas bit (CRC on boot will stop device if error is detected in boot areas)
#pragma config APPSCEN = OFF  // CRC on boot application code scan enable (CRC on boot will not include the application area of program memory in its calculation)
#pragma config SAFSCEN = OFF  // CRC on boot SAF area scan enable (CRC on boot will not include the SAF area of program memory in its calculation)
#pragma config DATASCEN = OFF // CRC on boot Data EEPROM scan enable (CRC on boot will not include data EEPROM in its calculation)
#pragma config CFGSCEN = OFF  // CRC on boot Config fuses scan enable (CRC on boot will not include the configuration fuses in its calculation)
#pragma config COE = HALT     // CRC on boot Continue on Error for non-boot areas bit (CRC on boot will stop device if error is detected in non-boot areas)
#pragma config BOOTPOR = OFF  // Boot on CRC Enable bit (CRC on boot will not run)

// CONFIG12
#pragma config BCRCPOLT = hFF // Boot Sector Polynomial for CRC on boot bits 31-24 (Bits 31:24 of BCRCPOL are 0xFF)

// CONFIG13
#pragma config BCRCPOLU = hFF // Boot Sector Polynomial for CRC on boot bits 23-16 (Bits 23:16 of BCRCPOL are 0xFF)

// CONFIG14
#pragma config BCRCPOLH = hFF // Boot Sector Polynomial for CRC on boot bits 15-8 (Bits 15:8 of BCRCPOL are 0xFF)

// CONFIG15
#pragma config BCRCPOLL = hFF // Boot Sector Polynomial for CRC on boot bits 7-0 (Bits 7:0 of BCRCPOL are 0xFF)

// CONFIG16
#pragma config BCRCSEEDT = hFF // Boot Sector Seed for CRC on boot bits 31-24 (Bits 31:24 of BCRCSEED are 0xFF)

// CONFIG17
#pragma config BCRCSEEDU = hFF // Boot Sector Seed for CRC on boot bits 23-16 (Bits 23:16 of BCRCSEED are 0xFF)

// CONFIG18
#pragma config BCRCSEEDH = hFF // Boot Sector Seed for CRC on boot bits 15-8 (Bits 15:8 of BCRCSEED are 0xFF)

// CONFIG19
#pragma config BCRCSEEDL = hFF // Boot Sector Seed for CRC on boot bits 7-0 (Bits 7:0 of BCRCSEED are 0xFF)

// CONFIG20
#pragma config BCRCEREST = hFF // Boot Sector Expected Result for CRC on boot bits 31-24 (Bits 31:24 of BCRCERES are 0xFF)

// CONFIG21
#pragma config BCRCERESU = hFF // Boot Sector Expected Result for CRC on boot bits 23-16 (Bits 23:16 of BCRCERES are 0xFF)

// CONFIG22
#pragma config BCRCERESH = hFF // Boot Sector Expected Result for CRC on boot bits 15-8 (Bits 15:8 of BCRCERES are 0xFF)

// CONFIG23
#pragma config BCRCERESL = hFF // Boot Sector Expected Result for CRC on boot bits 7-0 (Bits 7:0 of BCRCERES are 0xFF)

// CONFIG24
#pragma config CRCPOLT = hFF // Non-Boot Sector Polynomial for CRC on boot bits 31-24 (Bits 31:24 of CRCPOL are 0xFF)

// CONFIG25
#pragma config CRCPOLU = hFF // Non-Boot Sector Polynomial for CRC on boot bits 23-16 (Bits 23:16 of CRCPOL are 0xFF)

// CONFIG26
#pragma config CRCPOLH = hFF // Non-Boot Sector Polynomial for CRC on boot bits 15-8 (Bits 15:8 of CRCPOL are 0xFF)

// CONFIG27
#pragma config CRCPOLL = hFF // Non-Boot Sector Polynomial for CRC on boot bits 7-0 (Bits 7:0 of CRCPOL are 0xFF)

// CONFIG28
#pragma config CRCSEEDT = hFF // Non-Boot Sector Seed for CRC on boot bits 31-24 (Bits 31:24 of CRCSEED are 0xFF)

// CONFIG29
#pragma config CRCSEEDU = hFF // Non-Boot Sector Seed for CRC on boot bits 23-16 (Bits 23:16 of CRCSEED are 0xFF)

// CONFIG30
#pragma config CRCSEEDH = hFF // Non-Boot Sector Seed for CRC on boot bits 15-8 (Bits 15:8 of CRCSEED are 0xFF)

// CONFIG31
#pragma config CRCSEEDL = hFF // Non-Boot Sector Seed for CRC on boot bits 7-0 (Bits 7:0 of CRCSEED are 0xFF)

// CONFIG32
#pragma config CRCEREST = hFF // Non-Boot Sector Expected Result for CRC on boot bits 31-24 (Bits 31:24 of CRCERES are 0xFF)

// CONFIG33
#pragma config CRCERESU = hFF // Non-Boot Sector Expected Result for CRC on boot bits 23-16 (Bits 23:16 of CRCERES are 0xFF)

// CONFIG34
#pragma config CRCERESH = hFF // Non-Boot Sector Expected Result for CRC on boot bits 15-8 (Bits 15:8 of CRCERES are 0xFF)

// CONFIG35
#pragma config CRCERESL = hFF // Non-Boot Sector Expected Result for CRC on boot bits 7-0 (Bits 7:0 of CRCERES are 0xFF)

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.

#include <xc.h>

#define BUTTON_TIMER 0x60

#define ENA_INT()             \
    {                         \
        INTCON0bits.GIEH = 1; \
    }

static void read_analog();

static void led_on(void);
static void led_off(void);
static void UART_init(void);
static void UART_write(uint8_t);
static void read_analog(void);
static char get_button_state(void);
static char b2c(uint8_t, int);

char vh, vl;
char button, temp, temp2, cnt, vc;

void main(void)
{
    __asm("MOVLB 4");
    TRISA = 0x3;   // RA0, RA1 as input
    ANSELA = 0x01; // RA0 -> analog
    ADCON1 = 0;
    ADCON2 = 0;
    ADCON3 = 0;
    ADREF = 0; // Vref -> Vdd
    ADPCH = 0; // RA0 -> analog
    ADACQ = 0;
    ADCAP = 0;
    ADRPT = 0;
    ADACT = 0;
    ADCON0 = 0x94;
    WPUAbits.WPUA1 = 1;

    TRISC = 0x80; // RC7 as input
    ANSELC = 0x00;
    LATC = 0x4; // RC2 pull up

    U1RXPPS = 0x17; // UART1 Rx is RC7
    RC2PPS = 0x20;  // UART1 Tx is RC2

    UART_init();
    ENA_INT();
    led_off();
    button = 1;

    while (1)
    {
        temp = get_button_state();
        if (button == temp)
            continue;
        button = temp;

        if (!button)
        {
            read_analog();

            UART_write('T');
            UART_write('X');
            UART_write('D');
            UART_write('A');
            UART_write('\r');
            UART_write('\n');
            UART_write(' ');
            UART_write(' ');
            UART_write(' ');
            vc = b2c(vh, 0);
            UART_write(vc);
            vc = b2c(vl, 1);
            UART_write(vc);
            vc = b2c(vl, 0);
            UART_write(vc);
            UART_write('\n');
            UART_write('\0');
        }
    }
}

static void UART_write(uint8_t c)
{
    __asm("MOVLB 2");
    while (U1FIFObits.TXBF)
        ;
    U1TXB = c;
}

static void led_on(void)
{
    __asm("MOVLB 4");
    LATA |= 4;
}

static void led_off(void)
{
    __asm("MOVLB 4");
    LATA &= ~0x04;
}

static void UART_init(void)
{
    __asm("MOVLB 2");
    U1CON0 = 0x30;
    U1CON1 = 0;
    U1CON2 = 0x80;
    U1ERRIE = 0;
    U1UIR = 0;
    U1FIFO = 0;
    U1BRGH = 0;
    U1BRGL = 209;

    U1ERRIR = 0;
    U1CON1bits.ON = 1;
    __asm("MOVLB 4");
    PIR4bits.U1RXIF = 0;
    PIE4bits.U1RXIE = 1;
}

static char get_button_state(void)
{
    cnt = 0;
    __asm("MOVLB 3");
    T2PR = BUTTON_TIMER;
    TMR2 = 0;
    temp = PORTAbits.RA1;
    T2CONbits.ON = 1;

    while (TMR2 < BUTTON_TIMER)
    {
        temp2 = PORTAbits.RA1;
        if (!temp2)
        {
            cnt++;
        }
    }

    if (cnt > 10)
    {
        temp = 0;
        led_on();
    }
    else
    {
        temp = 1;
        led_off();
    }
    __asm("MOVLB 3");
    T2CONbits.ON = 0;
    while (!PORTAbits.RA1)
        ;

    return temp;
}

static void read_analog()
{
    __asm("MOVLB 3");
    ADCON0bits.GO = 1;
    while (ADCON0bits.GO)
        ;

    vh = ADRESH;
    vl = ADRESL;
}

static char b2c(uint8_t b, int high)
{
    if (high)
    {
        temp2 = (b & 0xf0) >> 4;
    }
    else
    {
        temp2 = (b & 0xf);
    }

    if (temp2 < 0xa)
    {
        temp2 += '0';
    }
    else
    {
        temp2 = temp2 - 0xa + 'A';
    }
    return temp2;
}