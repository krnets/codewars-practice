/*
Fix a bug in provided method which should execute a passed action n (possibly hundreds) times.
The method is timing out and not completing in time.
*/

public class Worker {
    public void execute(Runnable action, int nTimes) {
        int onStart = Thread.activeCount();
        for (int i = 0; i < nTimes; i++)
            new Thread(action).start();
        while (Thread.activeCount() != onStart) ;
    }
}
