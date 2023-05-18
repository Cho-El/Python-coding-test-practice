public class OuterClass2 {
    int field = 30;
    int getOuterClass() {
        OuterClass outerClass = new OuterClass();
        return new OuterClass().getField();
        // return new OuterClass().getField(); // 로 접근해야함
    }
}
