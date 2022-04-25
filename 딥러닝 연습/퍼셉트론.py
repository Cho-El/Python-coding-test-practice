class Logical_gate: # 논리 게이트
    def __init__(self, weight_dict):
        self.weight = weight_dict
    
    def Perceptron(self, x1, x2, key):
        weight = self.weight[key]
        w = weight['w']
        b = weight['b']

        y = w[0] * x1 + w[1] * x2 + b

        if y <= 0:
            return 0
        elif y >0:
            return 1

    def Run_Gate(self, key):
        print(key + ' Gate')
        print('----' * 20)
        print('(0, 0)', self.Perceptron(0,0,key))
        print('(0, 1)', self.Perceptron(0,1,key))
        print('(1, 0)', self.Perceptron(1,0,key))
        print('(1, 1)', self.Perceptron(1,1,key))
        print('----' * 20)
        print('\n')

weight_dict = {'AND':{'w' : [0.5,0.5], 'b':-0.5},
               'NAND':{'w' : [-0.5,-0.5], 'b':0.5},
               'OR':{'w' : [0.5,0.5], 'b':-0.2}}

LG = Logical_gate(weight_dict)
LG.Run_Gate('AND')
LG.Run_Gate('NAND')
LG.Run_Gate('OR')