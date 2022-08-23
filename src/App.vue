<script setup>
import { ref, reactive } from 'vue'


function round_mul5(val) {
  return Math.round(val / 5) * 5
}


var current_state = reactive({ day: 0, exercise: 0 })

/*
  Day 1 / Monday
*/

var day1BenchPress = ref([
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

var day1BentOverRow = ref([
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

var day1OverHeadPress = ref([
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

var day2Squat = ref([
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

var day2SumoDeadlift = ref([
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
var day3OverHeadPress = ref([
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

var day3BentOverRow = ref([
  { set: 1, multiplier: 0.40, weight: null, reps: "6", plates: null, done: false },
  { set: 2, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.60, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.60, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.60, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.60, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.60, weight: null, reps: "8", plates: null, done: false },
])

var day3InclineBench = ref([
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

var day4Deadlift = ref([
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

var day4FrontSquat = ref([
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

var day5BenchPress = ref([
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

var day5BentOverRow = ref([
  { set: 1, multiplier: 0.40, weight: null, reps: "6", plates: null, done: false },
  { set: 2, multiplier: 0.50, weight: null, reps: "5", plates: null, done: false },
  { set: 3, multiplier: 0.60, weight: null, reps: "3", plates: null, done: false },
  { set: 4, multiplier: 0.60, weight: null, reps: "5", plates: null, done: false },
  { set: 5, multiplier: 0.60, weight: null, reps: "7", plates: null, done: false },
  { set: 6, multiplier: 0.60, weight: null, reps: "4", plates: null, done: false },
  { set: 7, multiplier: 0.60, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.60, weight: null, reps: "8", plates: null, done: false },
])

var day5CloseGripBenchPress = ref([
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
    name: "Mon", exercises: [
      { name: "Bench Press", sets: day1BenchPress },
      { name: "Bent Over Row", sets: day1BentOverRow },
      { name: "Over Head Press", sets: day1OverHeadPress }]
  },
  {
    name: "Tue", exercises: [
      { name: "Squat", sets: day2Squat },
      { name: "Sumo Deadlift", sets: day2SumoDeadlift }],
  },
  {
    name: "Wed", exercises: [
      { name: "Over Head Press", sets: day3OverHeadPress },
      { name: "Bent Over Row", sets: day3BentOverRow },
      { name: "Incline Bench", sets: day3InclineBench }],
  },
  {
    name: "Thu", exercises: [
      { name: "Deadlift", sets: day4Deadlift },
      { name: "Front Squat", sets: day4FrontSquat }],
  },
  {
    name: "Fri", exercises: [
      { name: "Bench Press", sets: day5BenchPress },
      { name: "Bent Over Row", sets: day5BentOverRow },
      { name: "C.G. Bench Press", sets: day5CloseGripBenchPress }],
  },
])

var base_exercises = ref([
  { id: 0, name: "Bench Press", TM: 170, sets: [day1BenchPress, day3InclineBench, day5BenchPress, day5CloseGripBenchPress] },
  { id: 1, name: "Deadlift", TM: 270, sets: [day2SumoDeadlift, day4Deadlift] },
  { id: 2, name: "Over Head Press", TM: 95, sets: [day1OverHeadPress, day3OverHeadPress] },
  { id: 3, name: "Row", TM: 180, sets: [day1BentOverRow, day3BentOverRow, day5BentOverRow] },
  { id: 4, name: "Squat", TM: 165, sets: [day2Squat, day4FrontSquat] }
])

base_exercises.value.forEach((exercise) => {
  exercise.sets.forEach((sets) => {
    sets.value.forEach((set) => {
      set.weight = round_mul5(set.multiplier * exercise.TM);
      set.plates = getPlates(set.weight);
    })
  })
})

function round_mul10(val) {
  return Math.round(val / 10) * 10
}

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
  e.target.value = round_mul5(e.target.value)
  var exercise = base_exercises.value[e.target.id]
  exercise.TM = e.target.value
  exercise.sets.forEach((sets) => {
    sets.value.forEach((set) => {
      set.weight = round_mul5(set.multiplier * exercise.TM);
      set.plates = getPlates(set.weight);
    })
  })
}

const show_tm = ref(false)
function toggle() {
  show_tm.value = !show_tm.value
}

function select_day(i) {
  if (current_state.day == i) {
    return
  }
  current_state.day = i
  current_state.exercise = 0
}

function next_exercise() {
  var i = current_state.exercise
  var total = days.value[current_state.day].exercises.length
  if (i < total - 1) {
    current_state.exercise = current_state.exercise + 1
  } else {
    return
  }
}

function prev_exercise() {
  var i = current_state.exercise
  if (i >= 1) {
    current_state.exercise = current_state.exercise - 1
  } else {
    return
  }
}
</script>

<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
  <div class="card">
    <h2 class="big-button" @click="toggle">Training Max (TM) </h2>
    <div class="wrapper" :class="{ closed: !show_tm, open: show_tm }">
      <div class="card-content " v-for="(exercise, index) in base_exercises" :key="index">
        <div>{{ exercise.name }}</div>
        <input type="number" :value="exercise.TM" :id="index" @change="onChange" @focus="$event.target.select()">
      </div>
    </div>
  <div class="ribbon">
    <div class="tab" v-for="(day, index) in days" :key="index" :class="{ tab_selected: current_state.day == index }"
      @click="select_day(index)">{{ day.name }}</div>
  </div>
  </div>

  <div class="horizontal-scroll__container">
    <div class="horizontal-scroll__button" @click="prev_exercise"><img src="./assets/chevron_left.svg" alt="Previous" class="chevron_svg">
    </div>
    <div class="horizontal-scroll__item">{{ days[current_state.day].exercises[current_state.exercise].name }}</div>
    <div class="horizontal-scroll__button" @click="next_exercise"><img src="./assets/chevron_right.svg" alt="Next" class="chevron_svg">
    </div>
  </div>
  <div class="table-container">
    <div class="row row-heading">
      <div class="cell cell-heading">Weight</div>
      <div class="cell cell-heading">Reps</div>
      <div class="cell cell-heading">Plates</div>
      <div class="cell cell-heading">Done</div>
    </div>
    <div class="row" :class="{ done: set.done }"
      v-for="set in days[current_state.day].exercises[current_state.exercise].sets" :key="set.set">

      <div class="cell">{{ set.weight }}</div>
      <div class="cell">{{ set.reps }}</div>
      <div class="cell text-align-left"> <span :class="{
        chip_45: plate == 45,
        chip_35: plate == 35,
        chip_25: plate == 25,
        chip_10: plate == 10,
        chip_5: plate == 5,
        chip_2_5: plate == 2.5
      }" v-for="(plate, index) in set.plates" :key="index">{{ String(plate) == "2.5" ? "2½" : plate }}</span></div>
      <div class="cell"><input style="transform:scale(2)" type="checkbox" v-model="set.done"></div>
    </div>
  </div>

</template>


<style>
.done {
  opacity: 0.25;
  transition: opacity 0.25s;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>