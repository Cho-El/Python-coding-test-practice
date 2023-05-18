public class OuterClass {
    private int privateField = 2;
    static int staticOuterClassField = 10;
    int field = 10;
    int getField() {
        return field;
    }
    int getPrivateField() {
        return this.privateField;
    }
    class InnerClass {
        static int staticOuterClassField = 5;
        int inner_field = 20;
        public int getOuterfield() {
            staticOuterClassField ++;
            staticOuterClassField = OuterClass.staticOuterClassField;
            System.out.println("OuterClass staticOuterClassField : " + OuterClass.staticOuterClassField);
            System.out.println("InnerClass staticOuterClassField : " + staticOuterClassField);
            OuterClass.this.privateField = 5;
            return OuterClass.this.getField(); // 숨은 외부 참조가 있기 때문에 가능
        }
    }
}
