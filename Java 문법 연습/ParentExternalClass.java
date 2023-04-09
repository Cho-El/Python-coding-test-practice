interface InterfaceParentExternalClass {
    public abstract void mainLogic1(); // 모든 메소드는 public abstract이어야 합니다.
    public static final int importNum1 = 10; // 모든 필드는 public static final이어야 합니다.
    void mainLogic2(); // public abstract가 생략 됨 자동으로 컴파일러가 추가함
    int importNum2 = 11;
}

public class ParentExternalClass implements InterfaceParentExternalClass{
    private int parentPrNum;
    public int parentPuNum;
    public ParentExternalClass(int prNum, int puNum) {
        this.parentPrNum = prNum;
        this.parentPuNum = puNum;
    }
    @Override
    public void mainLogic1() {
        System.out.println("메인로직1, " + importNum1);
    }
    @Override
    public void mainLogic2() {
        System.out.println("메인로직2" + importNum2);
    }
}