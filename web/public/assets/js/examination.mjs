import {get, set, create} from './api.mjs'

export const ExaminationComponent = {
    data() {
        return {
            questions_and_answers: [],
            current_question: {id: null, text: null, answers: []},
            current_answer: null,
            questionNum: 1,
            isLast: false
        }
    },
    computed: {
        isTextAnswer() {
            return this.current_question.answers.length == 0
        },
        nextButtonName() {
            return !this.isLast ? "Следующий вопрос" : "Завершить"
        }
    },
    methods: {
        async next_question(event) {
            if(this.current_answer == null)
                return;

            this.questions_and_answers.push({question_id: this.current_question.id, answer: this.current_answer})

            const next_id = await (await set('/chain', this.questions_and_answers, true)).data

            if(next_id != null)
                this.current_question = await (await get("/questions/" + next_id)).data
            else
                this.$parent.show_result(this.questions_and_answers)

            this.current_answer = null
            this.questionNum += 1
        },
        async get_result() {
            console.log(this.questions_and_answers)
        }
    },
    async mounted () {
        const response = await get("/chain")

        this.current_question = await (await get("/questions/" + response.data)).data
    },
    template:
    `
    <div id="examination-container" class="d-flex flex-column justify-content-around align-items-center"><span id="question-title" class="d-flex justify-content-center">Вопрос №{{questionNum}}</span><span id="question" class="d-flex justify-content-center">{{current_question.text}}</span>
        <ul id="answers-group" class="list-group" v-if="!isTextAnswer">
            <li class="list-group-item" v-for="answerValue in current_question.answers">
                <div class="form-check">
                    <input class="form-check-input answer" type="radio" name="answer" :value="answerValue" v-model="current_answer"/>
                    <label class="form-check-label">{{answerValue}}</label>
                </div>
            </li>
        </ul>
        <textarea id="answer-text" v-if="isTextAnswer" name="answer" v-model="current_answer"></textarea>
        <button id="next-question" class="btn btn-secondary d-flex mx-auto justify-content-xl-center" type="button" v-on:click="next_question">Следующий вопрос</button>
    </div>
    `
}