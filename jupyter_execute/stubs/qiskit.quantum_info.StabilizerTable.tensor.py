#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info.operators import StabilizerTable

current = StabilizerTable.from_labels(['+I', '-X'])
other =  StabilizerTable.from_labels(['-Y', '+Z'])
print(current.tensor(other))

