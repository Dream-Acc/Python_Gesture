import numpy as np
import torch as t
from model import HandModel
from torch import nn
from torchnet import meter
from torch.autograd import Variable
import copy

# 手语集
label = ["bad", "birthday", "good", "he", "help", "home", "introduce", "late", "me", "meet",
         "name", "sit", "sorry", "today", "yesterday", "you"]
label_num = len(label)

targetX = [0 for xx in range(label_num)]
# target 标签独热码
target = []
for xx in range(label_num):
    target_this = copy.deepcopy(targetX)
    target_this[xx] = 1
    target.append(target_this)

lr = 1e-3  # 学习率
model_saved = 'checkpoints/model'  # 模型保存地址 模型保存地址即是label+.npz

# 模型定义
model = HandModel()
# 使用Adam优化器
optimizer = t.optim.Adam(model.parameters(), lr=lr)
# MultiLabelSoftMarginLoss 多标签交叉熵损失函数
criterion = nn.MultiLabelSoftMarginLoss()
# AverageValueMeter 计算所有数的平均值和标准差，统计几个epoch中损失的平均值
loss_meter = meter.AverageValueMeter()

# 训练40个epochs
epochs = 40
for epoch in range(epochs):
    print("epoch:" + str(epoch))
    # loss_meter.reset 重置(清空序列)
    loss_meter.reset()
    correct_count = 0
    all_count = 0
    for i in range(label_num):
        # 读取数据
        data = np.load('./npz_files/' + label[i] + ".npz", allow_pickle=True)
        data = data['data']
        # data_num 每个数据对应的长度
        data_num = len(data)
        # 对每个data进行训练
        for j in range(data_num):
            # t.tensor 生成新的张量
            xdata = t.tensor(data[j])
            # optimizer.zero_grad 将模型的参数梯度初始化为0
            optimizer.zero_grad()
            this_target = t.tensor(target[i]).float()
            # Variable是一个存放会变化值的地理位置，里面的值会不停变化
            input_, this_target = Variable(xdata), Variable(this_target)
            # 模型对应输出 此时为tensor 为对应标签的概率
            output = model(input_)
            # print(max(output))
            # print(output.tolist().index(max(output)))
            # outLabel 输出（预测）对应的标签
            outLabel = label[int(output.tolist().index(max(output)))]
            # targetLabel 真实标签
            targetIndex = target[i].index(1)
            targetLabel = label[targetIndex]
            # correct_count 预测成功的数量
            if targetLabel == outLabel:
                correct_count += 1
            # all_count总数量
            all_count += 1
            # unsqueeze 函数起升维的作用, 参数表示在哪个地方加一个维度。
            output = t.unsqueeze(output, 0)
            this_target = t.unsqueeze(this_target, 0)
            # criterion 计算损失值
            loss = criterion(output, this_target)
            # loss.backward 反向传播，计算当前梯度
            loss.backward()
            # optimizer.step 根据梯度更新网络参数
            optimizer.step()
            # 计算所得的函数损失值放入loss_meter中
            loss_meter.add(loss.data)
    # 输出此时预测正确率
    correct_rate = correct_count / all_count
    print("correct_rate:", str(correct_rate))
    # 保存模型
    t.save(model.state_dict(), '%s_%s.pth' % (model_saved, epoch))
