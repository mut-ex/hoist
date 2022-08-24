<script setup>
import { ref } from 'vue'
import VueCookies from 'vue-cookies'
import DaySelector from './components/DaySelector.vue'
import ExerciseSelector from './components/ExerciseSelector.vue'

function roundMul5(val) {
  return Math.round(val / 5) * 5
}

var current_exercise = ref(0)
var current_day = ref(0)
var current_lift_id = ref("day1BenchPress")

/*
  Day 1 / Monday
*/

var day1BenchPress = ref(JSON.parse(localStorage.getItem('day1BenchPress')) || [
  { set: 1, multiplier: 0.65, weight: null, reps: "8", plates: null, done: false },
  { set: 2, multiplier: 0.75, weight: null, reps: "6", plates: null, done: false },
  { set: 3, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 4, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 5, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 6, multiplier: 0.80, weight: null, reps: "5", plates: null, done: false },
  { set: 7, multiplier: 0.75, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "7", plates: null, done: false },
  { set: 9, multiplier: 0.65, weight: null, reps: "8+", plates: null, done: false },
])

var day1BentOverRow = ref(JSON.parse(localStorage.getItem('day1BentOverRow')) || [
  { set: 1, multiplier: 0.65, weight: null, reps: "8", plates: null, done: false },
  { set: 2, multiplier: 0.75, weight: null, reps: "6", plates: null, done: false },
  { set: 3, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 4, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 5, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 6, multiplier: 0.80, weight: null, reps: "5", plates: null, done: false },
  { set: 7, multiplier: 0.75, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "7", plates: null, done: false },
  { set: 9, multiplier: 0.65, weight: null, reps: "8+", plates: null, done: false },
])

var day1OverHeadPress = ref(JSON.parse(localStorage.getItem('day1OverHeadPress')) || [
  { set: 1, multiplier: 0.50, weight: null, reps: "6", plates: null, done: false },
  { set: 2, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.70, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.70, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.70, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.70, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.70, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "8", plates: null, done: false },
])

/*
  Day 2 / Tuesday
*/

var day2Squat = ref(JSON.parse(localStorage.getItem('day2Squat')) || [
  { set: 1, multiplier: 0.75, weight: null, reps: "5", plates: null, done: false },
  { set: 2, multiplier: 0.85, weight: null, reps: "3", plates: null, done: false },
  { set: 3, multiplier: 0.95, weight: null, reps: "1+", plates: null, done: false },
  { set: 4, multiplier: 0.90, weight: null, reps: "3", plates: null, done: false },
  { set: 5, multiplier: 0.85, weight: null, reps: "3", plates: null, done: false },
  { set: 6, multiplier: 0.80, weight: null, reps: "3", plates: null, done: false },
  { set: 7, multiplier: 0.75, weight: null, reps: "5", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "5", plates: null, done: false },
  { set: 9, multiplier: 0.65, weight: null, reps: "5+", plates: null, done: false },
])

var day2SumoDeadlift = ref(JSON.parse(localStorage.getItem('day2SumoDeadlift')) || [
  { set: 1, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 2, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.70, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.70, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.70, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.70, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.70, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "8", plates: null, done: false },
])


/*
  Day 3 / Wednesday
*/
var day3OverHeadPress = ref(JSON.parse(localStorage.getItem('day3OverHeadPress')) || [
  { set: 1, multiplier: 0.75, weight: null, reps: "5", plates: null, done: false },
  { set: 2, multiplier: 0.85, weight: null, reps: "3", plates: null, done: false },
  { set: 3, multiplier: 0.95, weight: null, reps: "1+", plates: null, done: false },
  { set: 4, multiplier: 0.90, weight: null, reps: "3", plates: null, done: false },
  { set: 5, multiplier: 0.85, weight: null, reps: "3", plates: null, done: false },
  { set: 6, multiplier: 0.80, weight: null, reps: "3", plates: null, done: false },
  { set: 7, multiplier: 0.75, weight: null, reps: "5", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "5", plates: null, done: false },
  { set: 9, multiplier: 0.65, weight: null, reps: "5+", plates: null, done: false },
])

var day3BentOverRow = ref(JSON.parse(localStorage.getItem('day3BentOverRow')) || [
  { set: 1, multiplier: 0.40, weight: null, reps: "6", plates: null, done: false },
  { set: 2, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.60, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.60, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.60, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.60, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.60, weight: null, reps: "8", plates: null, done: false },
])

var day3InclineBench = ref(JSON.parse(localStorage.getItem('day3InclineBench')) || [
  { set: 1, multiplier: 0.40, weight: null, reps: "6", plates: null, done: false },
  { set: 2, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.60, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.60, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.60, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.60, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.60, weight: null, reps: "8", plates: null, done: false },
])


/*
  Day 4 / Thursday
*/

var day4Deadlift = ref(JSON.parse(localStorage.getItem('day4Deadlift ')) || [
  { set: 1, multiplier: 0.75, weight: null, reps: "5", plates: null, done: false },
  { set: 2, multiplier: 0.85, weight: null, reps: "3", plates: null, done: false },
  { set: 3, multiplier: 0.95, weight: null, reps: "1+", plates: null, done: false },
  { set: 4, multiplier: 0.90, weight: null, reps: "3", plates: null, done: false },
  { set: 5, multiplier: 0.85, weight: null, reps: "3", plates: null, done: false },
  { set: 6, multiplier: 0.80, weight: null, reps: "3", plates: null, done: false },
  { set: 7, multiplier: 0.75, weight: null, reps: "3", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "3", plates: null, done: false },
  { set: 9, multiplier: 0.65, weight: null, reps: "3+", plates: null, done: false },
])

var day4FrontSquat = ref(JSON.parse(localStorage.getItem('day4FrontSquat')) || [
  { set: 1, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 2, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.70, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.70, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.70, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.70, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.70, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "8", plates: null, done: false },
])


/*
  Day 5 / Friday
*/

var day5BenchPress = ref(JSON.parse(localStorage.getItem('day5BenchPress')) || [
  { set: 1, multiplier: 0.75, weight: null, reps: "5", plates: null, done: false },
  { set: 2, multiplier: 0.85, weight: null, reps: "3", plates: null, done: false },
  { set: 3, multiplier: 0.95, weight: null, reps: "1+", plates: null, done: false },
  { set: 4, multiplier: 0.90, weight: null, reps: "3", plates: null, done: false },
  { set: 5, multiplier: 0.85, weight: null, reps: "5", plates: null, done: false },
  { set: 6, multiplier: 0.80, weight: null, reps: "3", plates: null, done: false },
  { set: 7, multiplier: 0.75, weight: null, reps: "5", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "3", plates: null, done: false },
  { set: 9, multiplier: 0.65, weight: null, reps: "5+", plates: null, done: false },
])

var day5BentOverRow = ref(JSON.parse(localStorage.getItem('day5BentOverRow')) || [
  { set: 1, multiplier: 0.40, weight: null, reps: "6", plates: null, done: false },
  { set: 2, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.60, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.60, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.60, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.60, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.60, weight: null, reps: "8", plates: null, done: false },
])

var day5CloseGripBenchPress = ref(JSON.parse(localStorage.getItem('day5CloseGripBenchPress')) || [
  { set: 1, multiplier: 0.40, weight: null, reps: "6", plates: null, done: false },
  { set: 2, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.60, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.60, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.60, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.60, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.60, weight: null, reps: "8", plates: null, done: false },
])


var days = ref([
  {
    name: "Mon", routines: [
      { id: "day1BenchPress", name: "Bench Press", sets: day1BenchPress },
      { id: "day1BentOverRow", name: "Bent Over Row", sets: day1BentOverRow },
      { id: "day1OverHeadPress", name: "Over Head Press", sets: day1OverHeadPress }]
  },
  {
    name: "Tue", routines: [
      { id: "day2Squat", name: "Squat", sets: day2Squat },
      { id: "day2SumoDeadlift", name: "Sumo Deadlift", sets: day2SumoDeadlift }],
  },
  {
    name: "Wed", routines: [
      { id: "day3OverHeadPress", name: "Over Head Press", sets: day3OverHeadPress },
      { id: "day3BentOverRow", name: "Bent Over Row", sets: day3BentOverRow },
      { id: "day3InclineBench", name: "Incline Bench", sets: day3InclineBench }],
  },
  {
    name: "Thu", routines: [
      { id: "day4Deadlift", name: "Deadlift", sets: day4Deadlift },
      { id: "day4FrontSquat", name: "Front Squat", sets: day4FrontSquat }],
  },
  {
    name: "Fri", routines: [
      { id: "day5BenchPress", name: "Bench Press", sets: day5BenchPress },
      { id: "day5BentOverRow", name: "Bent Over Row", sets: day5BentOverRow },
      { id: "day5CloseGripBenchPress", name: "C.G. Bench Press", sets: day5CloseGripBenchPress }],
  },
])

var base_exercises = ref([
  { name: "Bench Press", training_max: $cookies.isKey('Bench Press') ? $cookies.get('Bench Press') : 170, sets: [day1BenchPress, day3InclineBench, day5BenchPress, day5CloseGripBenchPress] },
  { name: "Deadlift", training_max: $cookies.isKey('Deadlift') ? $cookies.get('Deadlift') : 270, sets: [day2SumoDeadlift, day4Deadlift] },
  { name: "Over Head Press", training_max: $cookies.isKey('Over Head Press') ? $cookies.get('Over Head Press') : 95, sets: [day1OverHeadPress, day3OverHeadPress] },
  { name: "Row", training_max: $cookies.isKey('Row') ? $cookies.get('Row') : 180, sets: [day1BentOverRow, day3BentOverRow, day5BentOverRow] },
  { name: "Squat", training_max: $cookies.isKey('Squat') ? $cookies.get('Squat') : 165, sets: [day2Squat, day4FrontSquat] }
])

base_exercises.value.forEach((exercise) => {
  exercise.sets.forEach((sets) => {
    sets.value.forEach((set) => {
      set.weight = roundMul5(set.multiplier * exercise.training_max);
      set.plates = getPlates(set.weight);
    })
  })
})

function getPlate(weight) {
  if (weight < 2.5) {
    return weight
  }
  else if (weight >= 2.5 && weight < 5) {
    return 2.5
  }
  else if (weight >= 5 && weight < 10) {
    return 5
  }
  else if (weight >= 10 && weight < 25) {
    return 10
  }
  else if (weight >= 25 && weight < 35) {
    return 25
  }
  else if (weight >= 35 && weight < 45) {
    return 35
  }
  else if (weight >= 45) {
    return 45
  }
}

function getPlates(weight) {
  weight = (weight - 45) / 2
  var plates = []
  var plate
  while (weight != 0) {
    plate = getPlate(weight)
    if (plate >= 0) {
      plates[plates.length] = plate
    }
    weight = weight - plate
  }
  return plates
}

function onChange(e) {
  e.target.value = roundMul5(e.target.value)
  var exercise = base_exercises.value[e.target.id]
  exercise.training_max = e.target.value
  $cookies.set(exercise.name, exercise.training_max, '365d');
  exercise.sets.forEach((sets) => {
    sets.value.forEach((set) => {
      set.weight = roundMul5(set.multiplier * exercise.training_max);
      set.plates = getPlates(set.weight);
    })
  })
}

const show_training_max = ref(false)
const show_reset_menu = ref(false)


function toggle() {
  show_training_max.value = !show_training_max.value
}

function setDone(e, idx, set) {
  set.done = e.target.checked
  localStorage.setItem(current_lift_id.value, JSON.stringify(days.value[current_day.value].routines[current_exercise.value].sets))
}

function clearDoneThis() {
  days.value[current_day.value].routines[current_exercise.value].sets.forEach((set) => {
    set.done = false;
  })
  localStorage.setItem(current_lift_id.value, JSON.stringify(days.value[current_day.value].routines[current_exercise.value].sets))
}

function clearDoneToday(day) {
  days.value[day].routines.forEach((routine) => {
    routine.sets.forEach((set) => {
      set.done = false;
    })
    localStorage.setItem(routine.id, JSON.stringify(routine.sets))
  })
}

function clearDoneThisWeek() {
  for (let i = 0; i <= 4; i++) {
    clearDoneToday(i)
  }
}

function selectDay(value) {
  if (current_day.value == value) {
    return
  }
  current_day.value = value
  current_exercise.value = 0
  current_lift_id.value = days.value[current_day.value].routines[current_exercise.value].id
  no_more_left.value = true
  no_more_right.value = false
}

const no_more_right = ref(false)
const no_more_left = ref(true)


function nextExercise() {
  var total = days.value[current_day.value].routines.length
  var i = current_exercise.value
  if (i < total - 1) {
    current_exercise.value = current_exercise.value + 1
  }
  if (i == total - 2) {
    no_more_right.value = true
  }
  if (i >= 0) {
    no_more_left.value = false
  }
  current_lift_id.value = days.value[current_day.value].routines[current_exercise.value].id

}

function prevExercise() {
  var total = days.value[current_day.value].routines.length
  var i = current_exercise.value
  if (i > 0) {
    current_exercise.value = current_exercise.value - 1
  }
  if (i == 1) {
    no_more_left.value = true
  }
  if (i <= total - 1) {
    no_more_right.value = false
  }
  current_lift_id.value = days.value[current_day.value].routines[current_exercise.value].id

}
</script>

<template>
  <div class="logo"><img src="./assets/hoist_logo.svg" alt="Hoist">
  </div>
  <div class="card">
    <DaySelector :days="days" :current_day="current_day" @ev_day_selected="selectDay" />
  </div>
  <ExerciseSelector :no_more_right="no_more_right" :no_more_left="no_more_left"
    :curr_exercise_name="days[current_day].routines[current_exercise].name" @ev_prev_exercise="prevExercise"
    @ev_next_exercise="nextExercise" />
  <!-- <div class="horizontal-scroll__container">
    <div class="horizontal-scroll__button" @click="prevExercise" :class="{ hide: no_more_left }"><img
        src="./assets/chevron_left.svg" alt="Previous" class="horizontal-scroll__button__svg">
    </div>
    <div class="horizontal-scroll__item">{{ days[current_day].routines[current_exercise].name }}</div>
    <div class="horizontal-scroll__button" @click="nextExercise" :class="{ hide: no_more_right }"><img
        src="./assets/chevron_right.svg" alt="Next" class="horizontal-scroll__button__svg">
    </div>
  </div> -->
  <div class="table__container">
    <div class="row row--heading">
      <div class="cell border-right--darker">Weight</div>
      <div class="cell border-right--darker">Reps</div>
      <div class="cell border-right--darker">Plates</div>
      <div class="cell">Done</div>
    </div>
    <div class="row" :class="{ done: set.done, 'not-done': !set.done }"
      v-for="set in days[current_day].routines[current_exercise].sets" :key="set.set">
      <div class="cell border-right">{{ set.weight }}</div>
      <div class="cell border-right">{{ set.reps }}</div>
      <div class="cell border-right text-align-left flex"> <span class="chip" :class="{
        'chip--45': plate == 45,
        'chip--35': plate == 35,
        'chip--25': plate == 25,
        'chip--10': plate == 10,
        'chip--5': plate == 5,
        'chip--2_5': plate == 2.5
      }" v-for="(plate, index) in set.plates" :key="index">{{ plate }}</span></div>
      <div class="cell"><input type="checkbox" @click="setDone($event, set.set, set)" :checked="set.done"></div>
    </div>
  </div>
  <div class="card">
    <h2 class="big-button" @click="show_training_max = !show_training_max">Training Max</h2>
    <div class="wrapper" :class="{ closed: !show_training_max, open: show_training_max }">
      <div class="card__content " v-for="(exercise, index) in base_exercises" :key="index">
        <div>{{ exercise.name }}</div>
        <input type="number" :value="exercise.training_max" :id="index" @change="onChange"
          @focus="$event.target.select()">
      </div>
    </div>

    <h2 class="big-button" @click="show_reset_menu = !show_reset_menu">Clear Done</h2>
    <div class="wrapper" :class="{ closed: !show_reset_menu, open: show_reset_menu }">
      <div class="button-group">
        <h4 class="small-button" @click="clearDoneThis">This Lift</h4>
        <h4 class="small-button" @click="clearDoneToday(current_day)">Today's Lifts</h4>
        <h4 class="small-button" @click="clearDoneThisWeek">Entire Week</h4>
      </div>
    </div>
  </div>
</template>


<style>
.hide {
  visibility: hidden;
}

.done {
  opacity: 0.25;
  transition: opacity 0.25s;
}

.not-done {
  opacity: 1;
  transition: opacity 0.25s;
}
</style>