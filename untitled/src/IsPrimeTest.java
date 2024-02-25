import static org.junit.jupiter.api.Assertions.*;

class IsPrimeTest {

    @org.junit.jupiter.api.Test
    void isPrime1() {
        assertEquals(IsPrime.isPrime(1), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime2() {
        assertEquals(IsPrime.isPrime(2), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime3() {
        assertEquals(IsPrime.isPrime(3), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime4() {
        assertEquals(IsPrime.isPrime(4), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime5() {
        assertEquals(IsPrime.isPrime(5), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime6() {
        assertEquals(IsPrime.isPrime(6), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime7() {
        assertEquals(IsPrime.isPrime(7), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime8() {
        assertEquals(IsPrime.isPrime(8), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime9() {
        assertEquals(IsPrime.isPrime(9), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime10() {
        assertEquals(IsPrime.isPrime(10), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime11() {
        assertEquals(IsPrime.isPrime(11), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime12() {
        assertEquals(IsPrime.isPrime(12), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime13() {
        assertEquals(IsPrime.isPrime(13), true);
    }
}