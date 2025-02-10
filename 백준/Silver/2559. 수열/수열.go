// 질문게시판에 있는 코드 오류 찾기 위해 복붙
package main
import "fmt"
import "strings"
import "bufio"
import "strconv"
import "os"

func main() {
  br := bufio.NewReader(os.Stdin)
  in, _ := br.ReadString('\n')
  in = strings.TrimSpace(in)
  nums := strings.Split(in, " ")
  N, _ := strconv.Atoi(nums[0])
  K, _ := strconv.Atoi(nums[1])
  in, _ = br.ReadString('\n')
  nums = strings.Fields(in)
  sum := make([]int, N+1)
  max := 0
  for i := 1; i <= N; i++ {
    n, _ := strconv.Atoi(nums[i-1])
    if i == 1 {
      sum[i] = n
    } else {
      sum[i] = sum[i-1] + n
    }
    if i == K {
      max = sum[i]
    } else if i > K {
      sumK := sum[i] - sum[i-K]
      if sumK > max { max = sumK }
    }
  }
  fmt.Println(max)
}