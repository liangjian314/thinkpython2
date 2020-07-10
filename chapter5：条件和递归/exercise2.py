import time
a = int(time.time())
print(a)

s = a % 60
m_count = a//60
m = m_count % 60
h_count = m_count//60
h = h_count % 24
d = h_count // 24

print(d, h, m, s)
