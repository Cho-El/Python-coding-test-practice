public class PracticeClass1 {
    public static void main(String[] args){
        final ExternalClass externalClass = new ExternalClass(100,200);
        //  externalClass = new ExternalClass(); // final로 선언했으므로 재할당 불가능
        final Main2 main2 = new Main2(externalClass);
        String[] strArray = externalClass.returnPuStringArray();
        System.out.println("public int : " + externalClass.puNum);
        System.out.println("private int : " + externalClass.getprivateNum());
        System.out.print("배열 :");
        for(String s: strArray) {
            System.out.print(" " + s);
        }
        System.out.println();
        System.out.println("privateNum : " + externalClass.getprivateNum());
        executePrivateMethodInStaticMethod();
        Main2.executeNonStaticPublicMethodInStaticMethod();
        main2.printGetPrivateNuminMain2();

    }
    private static void executePrivateMethodInStaticMethod() {
        System.out.println("private Method execute in static method");
    }
    
}
class Main2 {
    private ExternalClass externalClass;

    public Main2(ExternalClass externalClass) {
        this.externalClass = externalClass;
    }
    public void printGetPrivateNuminMain2() {
        System.out.println("externalClassPrivateInt print in Main2 : " + this.externalClass.getprivateNum());
    }
    public static void executeNonStaticPublicMethodInStaticMethod() {
        System.out.println("Static Public Method execute in static method");
    }
}