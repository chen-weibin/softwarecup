import Vue from 'vue'
import SvgIcon from '@/components/svgicon/SvgIcon.vue'// svg component

// register globally
Vue.component(SvgIcon.name, SvgIcon)

const req = require.context('./svg', false, /\.svg$/)
const requireAll = requireContext => requireContext.keys().map(requireContext)
requireAll(req)
