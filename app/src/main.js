import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

import './icons' // 引入图标组件
import toast from './plugins' // 引入自定义组件
Vue.use(toast)
import router from './router'
import store from './store'

//echart的使用
import * as echarts from 'echarts/core' 
// 引入柱状图图表，图表后缀都为 Chart
import { LineChart } from 'echarts/charts';
// 引入提示框，标题，直角坐标系，数据集，内置数据转换器组件，组件后缀都为 Component
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  LegendComponent,
} from 'echarts/components';
// 标签自动布局，全局过渡动画等特性
import { LabelLayout, UniversalTransition } from 'echarts/features';
// 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
import { CanvasRenderer } from 'echarts/renderers';
// 注册必须的组件
echarts.use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  LineChart,
  LabelLayout,
  UniversalTransition,
  CanvasRenderer,
  LegendComponent,
])
Vue.prototype.$echarts = echarts


import Download from './components/download/Download'
Vue.component(Download.name, Download)

new Vue({
  render: h => h(App),
  router,
  store,
  beforeCreate() {
    Vue.prototype.$bus = this
  }
}).$mount('#app')


