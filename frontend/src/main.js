import { createApp } from 'vue'
import App from './App.vue'
import UserImage from './components/UserImage.vue'
import SearchBox from './components/SearchBox.vue'
import UtilityBox from './components/UtilityBox.vue'


const new_app = createApp(App)
new_app.component('user-image', UserImage)
new_app.component('search-box', SearchBox)
new_app.component('utility-box', UtilityBox)
new_app.mount('#top')
