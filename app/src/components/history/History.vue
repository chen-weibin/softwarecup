<template>
    <div class="history">
        <div class="container">
            <div class="ch">
                <div class="chart" id="chart"></div>
                <div class="tip" v-show="isyk">
                    <div class="tt">游客登录没有历史记录, 快去注册一个账号吧。 <span @click="zc">点击注册</span></div>
                    <img src="../../assets/没有历史记录.svg" alt="">
                </div>
            </div>
            <div class="top">
                <div class="tit">解译详情</div>
                <div class="swiper">
                    <ul ref="swiper">
                        <li>
                            <img src="../../assets/swipure1.png" alt="">
                        </li>
                        <li>
                            <img src="../../assets/swipure2.png" alt="">
                        </li>
                        <li>
                            <img src="../../assets/swipure3.png" alt="">
                        </li>
                        <li>
                            <img src="../../assets/swipure4.png" alt="">
                        </li>
                        <li>
                            <img src="../../assets/swipure5.png" alt="">
                        </li>
                        <li>
                            <img src="../../assets/swipure6.png" alt="">
                        </li>
                        <li>
                            <img src="../../assets/swipure7.png" alt="">
                        </li>
                        <li>
                            <img src="../../assets/swipure8.png" alt="">
                        </li>
                    </ul>
                    <div class="line">
                        <div v-for="(item, index) in 8" :key="index" :class="cu === index ? 'cu' : ''" @click="changeCu(index)"></div>
                    </div>
                </div>
            </div>
            <!-- <ul class="datas" ref="ul" v-if="items.length">
                <li class="item" v-for="item in items" :key="item.id" >
                    <div class="before">了解更多详情</div>
                    <div class="label" :class="item.labelColor">{{item.label}}</div>
                    <div class="time">{{item.time}}</div>
                </li>
            </ul>
            <div v-else class="els">
                <div class="tttt">当前没有历史记录，快去试试吧</div>
                <img src="../../assets/没有历史记录.svg" alt="">
            </div> -->
        </div>
    </div>
</template>

<script>
    import {getHistory, getGraphData} from '@/api'
    import {getCookie} from '@/utils/cookie'
    export default {
        name: 'History',
        data() {
            return {
                // items: [],
                chart: null,
                xaxis: [], //x轴的时间
                yaxisChange: [], //y轴的数据
                yaxisClassification: [],
                yaxisdiwu: [],
                yaxisppyolo: [],
                style: {
                    fontColor: 'black',
                }, //主题
                isyk: false,
                cu: 0,
            }
        },
        mounted() {
           this.initCharts();
           setInterval(() => {
                if (this.cu < 7) {
                    this.$refs.swiper.style.transition= 'all 1s'
                    this.$refs.swiper.style.left = -350 * ++this.cu + 'px'
                } else {
                    this.$refs.swiper.style.transition= 'all 0s'
                    this.$refs.swiper.style.left = '0px'
                    this.cu = 0
                }
           }, 4000)       
        },
        methods: {
            initCharts() {
                this.chart = this.$echarts.init(document.getElementById("chart"));
                this.setOptions();
                window.addEventListener("resize", () => {
                    this.chart.resize();
                });
            },
            setOptions() {
                const echarts = this.$echarts
                this.chart.setOption({
                    title: {
                        text: '使用情况',
                        textStyle: {
                            color: this.style.fontColor,
                            fontSize: 19
                        },
                        left: 'center',
                        top: '15px',
                    },
                    tooltip: {
                        trigger: 'axis',
                        valueFormatter: (value) => value + '次'
                    },
                    legend: {
                        top: "45px",
                        right: '0px',
                        textStyle: {
                            color: this.style.fontColor,
                            fontSize: "13",
                            fontWeight: 300,
                        },
                        data: ['目标提取', '变化检测', '目标检测', '地物分类']
                    },
                    grid: {
                        left: "0",
                        top: "50",
                        right: "0",
                        bottom: "10",
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data: this.xaxis,
                            axisLabel: {
                                align: 'left',
                                color: this.style.fontColor, //rgba(255,255,255,.6)
                                fontSize: 12,
                                interval: 1,  //为了所有的x轴的标识都能显示
                                formatter: function (value) {
                                    return value.substring(8)
                                }
                            },
                            // x轴线的颜色为   rgba(255,255,255,.2)
                            axisLine: {
                                show: false
                                // lineStyle: {
                                //     color: this.style.xlinelColor //rgba(255,255,255,.2)
                                // }
                            },
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            axisTick: { show: false },
                            axisLine: {
                                show: false,
                                // lineStyle: {
                                //     color: "black" //rgba(255,255,255,.1)
                                // }
                            },
                            axisLabel: {
                                show: false,
                                // color: "white", //rgba(255,255,255,.6)
                                // fontSize: 12
                            },
                            // 修改分割线的颜色
                            splitLine: {
                                show: false,
                                // lineStyle: {
                                //     color: "rgba(255,255,255,.1)"
                                // }
                            }
                        }
                    ],
                    series: [
                        {
                            name: '目标提取',
                            type: 'line',
                            // stack: '总量',
                            smooth: true,
                            lineStyle: {
                                color: "#FFDE00",
                                width: 2
                            },
                            areaStyle: {
                                color: new echarts.graphic.LinearGradient(
                                    0,
                                    0,
                                    0,
                                    1,
                                    [
                                    {
                                        offset: 0,
                                        color: "rgba(255, 222, 0, 0.4)"  //rgb(255, 222, 0)
                                    },
                                    {
                                        offset: 0.8,
                                        color: "rgba(255, 222, 0, 0.1)"
                                    }
                                    ],
                                    false
                                ),
                                shadowColor: "rgba(0, 0, 0, 0.1)"
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            // 设置拐点 小圆点
                            symbol: "circle",
                            // 拐点大小
                            symbolSize: 5,
                            // 设置拐点颜色以及边框
                            itemStyle: {
                                color: "#FFDE00",
                                borderColor: "rgba(221, 220, 107, .1)",
                                borderWidth: 12
                            },
                            // 开始不显示拐点， 鼠标经过显示
                            showSymbol: false,
                            data: this.yaxisdiwu
                        },
                        {
                            name: '变化检测',
                            type: 'line',
                            // stack: '总量',
                            smooth: true,
                            lineStyle: {
                                color: "#678ffd", //#0184d5  #678ffd
                                width: 2 
                            },
                            // 填充区域
                            areaStyle: {
                                // 渐变色，只需要复制即可
                                color: new echarts.graphic.LinearGradient(
                                0,
                                0,
                                0,
                                1,
                                [
                                    {
                                    offset: 0,
                                    color: "rgba(103, 143, 253, 0.4)"   // 渐变色的起始颜色
                                    },
                                    {
                                    offset: 0.8,
                                    color: "rgba(103, 143, 253, 0.1)"   // 渐变线的结束颜色
                                    }
                                ],
                                false
                                ),
                                shadowColor: "rgba(0, 0, 0, 0.1)"
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            // 设置拐点 小圆点
                            symbol: "circle",
                            // 拐点大小
                            symbolSize: 8,
                            // 设置拐点颜色以及边框
                            itemStyle: {
                                color: "#678ffd",
                                borderColor: "rgba(221, 220, 107, .1)",
                                borderWidth: 12
                            },
                            // 开始不显示拐点， 鼠标经过显示
                            showSymbol: false,
                            data: this.yaxisChange
                        },
                        {
                            name: '目标检测',
                            type: 'line',
                            // stack: '总量',
                            smooth: true,
                            lineStyle: {
                                color: "#ff0066",
                                width: 2
                            },
                            areaStyle: {
                                color: new echarts.graphic.LinearGradient(
                                    0,
                                    0,
                                    0,
                                    1,
                                    [
                                    {
                                        offset: 0,
                                        color: "rgba(255, 0, 102, 0.4)"
                                    },
                                    {
                                        offset: 0.8,
                                        color: "rgba(255, 0, 102, 0.1)"
                                    }
                                    ],
                                    false
                                ),
                                shadowColor: "rgba(0, 0, 0, 0.1)"
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            // 设置拐点 小圆点
                            symbol: "circle",
                            // 拐点大小
                            symbolSize: 5,
                            // 设置拐点颜色以及边框
                            itemStyle: {
                                color: "#ff0066",
                                borderColor: "rgba(221, 220, 107, .1)",
                                borderWidth: 12
                            },
                            // 开始不显示拐点， 鼠标经过显示
                            showSymbol: false,
                            data: this.yaxisppyolo
                        },
                        {
                            name: '地物分类',
                            type: 'line',
                            // stack: '总量',
                            smooth: true,
                            lineStyle: {
                                color: "#00d887",
                                width: 2
                            },
                            areaStyle: {
                                color: new echarts.graphic.LinearGradient(
                                    0,
                                    0,
                                    0,
                                    1,
                                    [
                                    {
                                        offset: 0,
                                        color: "rgba(0, 216, 135, 0.4)"
                                    },
                                    {
                                        offset: 0.8,
                                        color: "rgba(0, 216, 135, 0.1)"
                                    }
                                    ],
                                    false
                                ),
                                shadowColor: "rgba(0, 0, 0, 0.1)"
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            // 设置拐点 小圆点
                            symbol: "circle",
                            // 拐点大小
                            symbolSize: 5,
                            // 设置拐点颜色以及边框
                            itemStyle: {
                                color: "#00d887",
                                borderColor: "rgba(221, 220, 107, .1)",
                                borderWidth: 12
                            },
                            // 开始不显示拐点， 鼠标经过显示
                            showSymbol: false,
                            data: this.yaxisClassification
                        }
                    ]
                })
            },
            zc(){
                this.$router.push({path: '/login'})
            },
            changeCu(index) {
                this.cu = index
                this.$refs.swiper.style.transition= 'all 0s'
                this.$refs.swiper.style.left = -350 * index + 'px'
            }
        },
        watch: {
            '$store.state.theme': {
                handler() {
                    let {style} = this
                    switch(this.$store.state.theme){
                        case 'light':
                            style.fontColor = 'black'
                            break
                        case 'dark':
                            style.fontColor = 'white'
                            break
                    }
                    this.$nextTick(() => {
                        this.setOptions()
                    })
                }
            }
        },
        activated(){
            const cookie = getCookie('xmut')
            if (cookie) {
                if (cookie === '999999') {
                    this.xaxis = ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none']
                    this.yaxisChange = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.yaxisClassification = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.yaxisdiwu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.yaxisppyolo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.isyk = true
                } else {
                    getGraphData({token: cookie}).then((response) => {
                        const {xaxis, yaxisChange, yaxisClassification, yaxisdiwu, yaxisppyolo} = response.data
                        this.xaxis = xaxis
                        this.yaxisChange = yaxisChange
                        this.yaxisClassification = yaxisClassification
                        this.yaxisdiwu = yaxisdiwu
                        this.yaxisppyolo = yaxisppyolo
                        this.setOptions()
                    }, error => {})
                }
            } else {
                this.$router.push({path: '/login'})
            }
            // const cookie = getCookie('xmut')
            // if (cookie && cookie !== '999999') {
            //     getHistory({token: cookie}).then((response) => {
            //         this.items = response.data.data
            //     }, error => {})
            // } else if (!cookie) {
            //     this.$router.push({path: '/login'})
            // }
        }
    }
</script>

<style lang='less' scoped>
    .history {
        float: right;
        width: calc(100% - 1100px);
        height: 100%;
        padding: 30px 45px 55px 10px;
    }
    .container {
        width: 100%;
        height: 100%;
        background-color: var(--history-bg);
        border-radius: 8px;
        position: relative;
        overflow: hidden;
    }

    .ch {
        position: absolute;
        bottom: 0px;
        left: 0;
        width: 100%;
        height: 330px;
        // position: relative;
    }
    .chart {
        width: 100%;
        height: 100%;
        background: var(--main-bg);
    }
    .tip {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        .tt {
            position: absolute;
            left: 20px;
            bottom: 40px;
            height: 30px;
            line-height: 30px;
            font-size: 15px;
            color: #00e092;
            span {
                color: #759aff;
                cursor: pointer;
            }
        }
        img {
            width: 100%;
            height: 100%;
        }
    }


    .top {
        width: 100%;
        height: 260px;
        overflow: hidden;
        // display: flex;
        // justify-content: center;
        // align-items: center;
        .tit {
            width: 100%;
            height: 40px;
            line-height: 40px;
            text-align: center;
            color: var(--main-font-color);
            font-size: 19px;
            font-weight: 700;
        }
        .swiper {
            width: 350px;
            transform: translateX(15px);
            height: 220px;
            overflow: hidden;
            position: relative;
            border-radius: 7px;
            .line {
                position: absolute;
                width: 240px;
                height: 3px;
                bottom: 5px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                justify-content: center;
                align-items: center;
                div {
                    width: 22px;
                    margin: 0 4px;
                    height: 100%;
                    border-radius: 2px;
                    background: rgb(255, 255, 255);
                    cursor: pointer;
                    &:hover {
                        background: #4576ff;
                    }
                }
                .cu {
                    background: #4576ff;
                }
            }
            ul {
                height: 100%;
                list-style: none;
                width: calc(350px * 8);
                position: absolute;
                top: 0;
                left: 0px;
                li {
                    float: left;
                    width: 350px;
                    height: 220px;
                    img {
                        width: 100%;
                        height: 100%;
                    }
                }
            }
        }
    }

    
    // .datas {
    //     list-style: none;
    //     padding: 10px 10px;
    //     overflow-y: auto;
    //     width: 100%;
    //     height: 100%;
    //     .item {
    //         width: 100%;
    //         height: 60px;
    //         border-radius: 5px;
    //         margin-bottom: 10px;
    //         position: relative;
    //         background-color: var(--history-item-bg-color);
    //         transition: all .2s;
    //         cursor: pointer;

    //         .target-extraction {
    //             background-color: #7B9EFE;
    //         }
    //         .change-detection {
    //             background-color: #9b6cfa;
    //         }
    //         .target-detection {
    //             background-color: #ed725a;
    //         }
    //         .terrain-classification {
    //             background-color: #5b59a6;
    //         }

    //         .before {
    //             padding: 4px 5px;
    //             font-size: 17px;
    //             height: 24px;
    //             color: var(--history-item-before);
    //             overflow: hidden;
    //             text-overflow: ellipsis;
    //             display: -webkit-box;
    //             -webkit-line-clamp: 1;
    //             -webkit-box-orient: vertical;
    //         }
    //         .label {
    //             position: absolute;
    //             left: 5px;
    //             top: 30px;
    //             height: 21px;
    //             line-height: 21px;
    //             text-align: center;
    //             color: var(--history-item-label);
    //             font-size: 14px;
    //             width: 70px;
    //             border-radius: 3px;
    //         }
    //         .time {
    //             position: absolute;
    //             left: 80px;
    //             top: 30px;
    //             height: 21px;
    //             line-height: 21px;
    //             color: var(--history-item-time);
    //             font-size: 13px;
    //             padding-left: 4px;
    //         }
    //         &:hover {
    //             transform: translateY(-1px);
    //             box-shadow: 6px 6px 20px rgba(118, 118, 118, 0.5);
    //         }
    //     }
    //     &::-webkit-scrollbar{
    //         width: 9px;
    //         background-color: transparent;
    //     }
    //     &::-webkit-scrollbar-track{
    //         border-radius: 5px;
    //         background: var(--history-scroll-track);
    //     }
    //     &::-webkit-scrollbar-thumb{
    //         border-radius: 5px;
    //         background: var(--history-scroll-thumb);
    //     }
    //     &::-webkit-scrollbar-thumb:hover{
    //         background: var(--history-scroll-hover);
    //     }
    // }

    // .els {
    //     width: 100%;
    //     height: 100%;
    //     display: flex;
    //     position: relative;  
    //     img {
    //         width: 100%;
    //     }
    //     .tttt {
    //         position: absolute;
    //         color: #8aa9fe;
    //         font-size: 18px;
    //         width: 100%;
    //         text-align: center;
    //         bottom: 100px;
    //     }
    // }



</style>