from unittest.mock import Mock

# Mock 객체 생성
mock = Mock()

# 임의로 반환값 지정
mock.return_value = 10

# 호출
result = mock()
print(result)  # 10

# 호출 기록 확인
mock.assert_called_once()
