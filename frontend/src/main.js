import { createApp } from 'vue'
import App from './App.vue'
import ComImage from './components/ComImage.vue'
import SearchBox from './components/SearchBox.vue'
import UtilityBox from './components/UtilityBox.vue'
import ChatBox from './components/lower/ChatBox.vue'



const new_app = createApp(App)
new_app.component('com-image', ComImage)
new_app.component('search-box', SearchBox)
new_app.component('utility-box', UtilityBox)

// lower sections
new_app.component('chat-box', ChatBox)

new_app.mount('#App')
