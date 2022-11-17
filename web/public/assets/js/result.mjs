import {get, set, create} from './api.mjs'

export const ResultComponent = {
    props: ['questions_and_answers'],
    data() {
        return {
            result: {title: null, text: null}
        }
    },
    methods: {
        return_home(event) {
            this.$parent.restart()
        }
    },
    async mounted () {
        console.log(this.questions_and_answers)
        this.result = await (await create("/answers", this.questions_and_answers)).data
    },
    template:
    `
    <div id="result-container" class="d-flex flex-column justify-content-around align-items-center">
        <span id="result-title" style="font-weight: bold;font-size: 30px;margin-bottom: 12px;">{{result.title}}</span>
        <span id="result-text" style="font-size: 18px;font-style: italic;">{{result.text}}</span>
        <button id="return_home_button" class="btn btn-secondary btn-lg" type="button" v-on:click="return_home">На главную</button>
    </div>
    `
}