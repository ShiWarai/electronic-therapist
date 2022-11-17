import {get} from "./api.mjs"
import {ExaminationComponent} from "./examination.mjs"
import {ResultComponent} from "./result.mjs"


const ElectronicTherapistApp = {
    data() {
        return {
            current_page: null,
            questions_and_answers: []
        }
    },
    methods: {
        start_examination() {
            this.current_page = 'examination'
        },
        show_result(questions_and_answers) {
            this.questions_and_answers = questions_and_answers
            this.current_page = 'result'
        },
        restart() {
            this.questions_and_answers = null
            this.current_page = 'welcome'
        }
    },
    mounted () {
        this.current_page = 'welcome'
    },
    components: 
    {
        ExaminationComponent,
        ResultComponent
    }
}

const app = Vue.createApp(ElectronicTherapistApp);
app.mount('#body');