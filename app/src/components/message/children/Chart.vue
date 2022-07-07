<template>
  <div class="ch">
    <div class="chart" id="chart"></div>
    <div class="tip" v-show="isyk">
        <div class="tt">游客登录没有历史记录, 快去注册一个账号吧。 <span @click="zc">点击注册</span></div>
        <img src="../../../assets/没有历史记录.svg" alt="">
    </div>
  </div>
</template>

<script>
    import {getGraphData} from '@/api'
    import {getCookie} from '@/utils/cookie'
    export default {
        name: "Chart",
        data() {
            return {
                chart: null,
                xaxis: [], //x轴的时间
                yaxisChange: [], //y轴的数据
                yaxisClassification: [],
                style: {
                    fontColor: 'black',
                }, //主题
                isyk: false,
            };
        },
        created(){
            // 请求数据
            const cookie = getCookie('xmut')
            if (cookie) {
                if (cookie === '999999') {
                    this.xaxis = ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none']
                    this.yaxisChange = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.yaxisClassification = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.isyk = true
                } else {
                    getGraphData({token: cookie}).then((response) => {
                        const {xaxis, yaxisChange, yaxisClassification} = response.data
                        this.xaxis = xaxis
                        this.yaxisChange = yaxisChange
                        this.yaxisClassification = yaxisClassification
                        this.setOptions()
                    }, error => {})
                }
            } else {
                this.$router.push({path: '/login'})
            }
        },
        mounted() {
            this.initCharts();
        },
        activated(){
            const cookie = getCookie('xmut')
            if (cookie) {
                if (cookie === '999999') {
                    this.xaxis = ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none']
                    this.yaxisChange = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.yaxisClassification = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    this.isyk = true
                } else {
                    getGraphData({token: cookie}).then((response) => {
                        const {xaxis, yaxisChange, yaxisClassification} = response.data
                        this.xaxis = xaxis
                        this.yaxisChange = yaxisChange
                        this.yaxisClassification = yaxisClassification
                        this.setOptions()
                    }, error => {})
                }
            } else {
                this.$router.push({path: '/login'})
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
                            fontSize: 20
                        },
                        left: '10px',
                        top: '10px',
                    },
                    tooltip: {
                        trigger: 'axis',
                        valueFormatter: (value) => value + '次'
                    },
                    legend: {
                        top: "10px",
                        right: '20px',
                        textStyle: {
                            color: this.style.fontColor,
                            fontSize: "13",
                            fontWeight: 300,
                        },
                        data: ['变化检测', '地物分类']
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
            }
        }
    };
</script>

<style lang='less' scoped>
    .ch {
        width: 100%;
        height: 100%;
        position: relative;
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
</style>