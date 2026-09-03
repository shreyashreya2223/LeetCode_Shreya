import java.util.*;

class Router {

    private int memoryLimit;
    private Queue<int[]> queue;
    private Set<String> packetSet;
    private Map<Integer, List<Integer>> destMap;

    public Router(int memoryLimit) {
        this.memoryLimit = memoryLimit;
        this.queue = new LinkedList<>();
        this.packetSet = new HashSet<>();
        this.destMap = new HashMap<>();
    }

    public boolean addPacket(int source, int destination, int timestamp) {
        String key = source + "#" + destination + "#" + timestamp;

        // Duplicate check
        if (packetSet.contains(key)) {
            return false;
        }

        // Remove oldest packet if memory limit exceeded
        if (queue.size() == memoryLimit) {
            removeOldestPacket();
        }

        int[] packet = new int[]{source, destination, timestamp};
        queue.offer(packet);
        packetSet.add(key);

        destMap.putIfAbsent(destination, new ArrayList<>());
        destMap.get(destination).add(timestamp);

        return true;
    }

    public int[] forwardPacket() {
        if (queue.isEmpty()) {
            return new int[]{};
        }

        int[] packet = queue.poll();

        int source = packet[0];
        int destination = packet[1];
        int timestamp = packet[2];

        String key = source + "#" + destination + "#" + timestamp;
        packetSet.remove(key);

        // Remove timestamp from destination map
        List<Integer> list = destMap.get(destination);
        list.remove(0); // FIFO timestamps due to non-decreasing timestamps

        if (list.isEmpty()) {
            destMap.remove(destination);
        }

        return packet;
    }

    public int getCount(int destination, int startTime, int endTime) {
        if (!destMap.containsKey(destination)) {
            return 0;
        }

        List<Integer> list = destMap.get(destination);

        int left = lowerBound(list, startTime);
        int right = upperBound(list, endTime);

        return right - left;
    }

    private void removeOldestPacket() {
        int[] packet = queue.poll();

        int source = packet[0];
        int destination = packet[1];
        int timestamp = packet[2];

        String key = source + "#" + destination + "#" + timestamp;
        packetSet.remove(key);

        List<Integer> list = destMap.get(destination);
        list.remove(0);

        if (list.isEmpty()) {
            destMap.remove(destination);
        }
    }

    // First index >= target
    private int lowerBound(List<Integer> list, int target) {
        int left = 0, right = list.size();

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (list.get(mid) >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    // First index > target
    private int upperBound(List<Integer> list, int target) {
        int left = 0, right = list.size();

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (list.get(mid) > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * boolean param_1 = obj.addPacket(source,destination,timestamp);
 * int[] param_2 = obj.forwardPacket();
 * int param_3 = obj.getCount(destination,startTime,endTime);
 */