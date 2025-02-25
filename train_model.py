import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

# 더미 학습 데이터
X = np.array([[0], [1], [2], [3], [4], [5]])
y = np.array([0, 0, 0, 1, 1, 1])

# 간단한 로지스틱 회귀 모델 학습
model = LogisticRegression()
model.fit(X, y)

# 모델 저장
joblib.dump(model, "app/model.pkl")
print("✅ 모델이 저장되었습니다!")