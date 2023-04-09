public class ExternalClass extends ParentExternalClass{

    // 필드 선언
    private int prNum; // private 접근 제어자 인스턴스 변수
    public int puNum; //  public 접근 제어자 인스턴스 변수
    final static int finalStaticNum = 10; // final과 static은 둘이 호응이 좋다. -> final static 값은 바꿀 수없다.
    static int staticNum = 11; // 값을 바꿀 수 있고, 해당 클래스로 생성된 객체는 이 값으 공유한다.

    public ExternalClass(int puNum, int prNum) { // 생성자
        super(prNum,puNum); // 부모 생성자 매개 변수
        this.puNum = 2;
        this.prNum = 1;
    }
    public String[] returnPuStringArray() {
        String[] result = {"1","2","3","4","5"};
        String[] prS = returnPrStringArray();
        result[0]+= prS[0];
        return result;
    }
    public int getprivateNum() {
        return this.prNum;
    }
    private String[] returnPrStringArray() {
        String[] result = {"1","2"};
        return result;
    }
}