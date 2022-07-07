<template>
    <div class="information">
        <div class="title">
            信息
        </div>
        <ul class="datas">
            <li class="item">
                模型训练
                <div class="desc">
                    BIT模型 —— 计算机视觉领域最先进的迁移学习模型
                </div>
            </li>
            <li class="item">
                优化策略
                <div class="desc">
                    上采样 —— 采用双三次插值
                </div>
            </li>
            <li class="item">
                图像分割
                <div class="desc">
                    ResNet —— 网络中引入恒等映射
                </div>
            </li>
            <li class="item">
                注意力机制
                <div class="desc">
                    SENET —— 最大程度上减少模型的错误率
                </div>
            </li>
            <li class="item">
                数据增强
                <div class="desc">
                    RandomVerticalFlip、RandomDistort、RandomBlur
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'Information',

    }
</script>

<style lang='less' scoped>
    .information {
        width: 100%;
        height: 100%;
        padding: 10px 15px;
        background: var(--information-bg);
    }
    .title {
        width: 100%;
        height: 40px;
        text-align: left;
        font-size: 20px;
        color: var(--information-title-color);
        font-weight: 700;
    }
    .datas {
        list-style: none;
        .item {
            padding-left: 20px;
            position: relative;
            width: 100%;
            height: 65px;
            font-size: 18px;
            color: var(--information-item-color);
            font-weight: 700;
            &::before {
                display: block;
                position: absolute;
                content: '';
                left: 6px;
                top: 9px;
                width: 8px;
                height: 8px;
                border-radius: 50%;
            }
            .desc {
                position: absolute;
                left: 55px;
                top: 30px;
                font-size: 16.5px;
                color: var(--information-desc-color);
                font-weight: 500;
            }
        }
        .item {
            &:nth-child(1)::before {
                background-color: var(--information-one-color);
            }
            &:nth-child(2)::before {
                background-color: var(--information-two-color);
            }
            &:nth-child(3)::before {
                background-color: var(--information-three-color);
            }
            &:nth-child(4)::before {
                background-color: var(--information-four-color);
            }
            &:nth-child(5)::before {
                background-color: var(--information-five-color);
            }
        }
    }
</style>