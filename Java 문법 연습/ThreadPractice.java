import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPractice {
    //Tread 사용하지 않는 코드
    public static void main2(String[] args) {
        // 작업 1 - 1.5초 소요
        System.out.println("작업1 시작");
        try {
            Thread.sleep(1500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("작업1 종료");

        // 작업 2 - 0.5초 소요
        System.out.println("작업2 시작");
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("작업2 종료");
    }
    public static void main(String[] args) {
        ExecutorService executorService = Executors.newCachedThreadPool();

        // 작업1 (스레드)
        executorService.submit(() -> {
            log("작업 1 시작");
            try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            log("작업 1 종료");
        });

        // 작업2
        log("작업 2 시작");
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        log("작업 2 종료");

        executorService.shutdown();
    }

    // 출력을 어떤 스레드에서 하고 있는지 확인
    private static void log(String content) {
        System.out.println(Thread.currentThread().getName() + "> " + content);
    }
}
