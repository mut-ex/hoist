<script setup>
import { ref } from 'vue'


function round_mul5(val) {
  return Math.round(val / 5) * 5
}

var benchpress_day1_sets = ref([
  { set: 1, multiplier: 0.65, weight: null, reps: "8", plates: null, done: false },
  { set: 2, multiplier: 0.75, weight: null, reps: "6", plates: null, done: false },
  { set: 3, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 4, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 5, multiplier: 0.85, weight: null, reps: "4", plates: null, done: false },
  { set: 6, multiplier: 0.80, weight: null, reps: "5", plates: null, done: false },
  { set: 7, multiplier: 0.75, weight: null, reps: "6", plates: null, done: false },
  { set: 8, multiplier: 0.70, weight: null, reps: "7", plates: null, done: false },
  { set: 9, multiplier: 0.65, weight: null, reps: "8", plates: null, done: false },
])

var row_day1_sets = ref([
  { set: 1, multiplier: 0.65, weight: null, reps: "8", plates: null },
  { set: 2, multiplier: 0.75, weight: null, reps: "6", plates: null },
  { set: 3, multiplier: 0.85, weight: null, reps: "4", plates: null },
  { set: 4, multiplier: 0.85, weight: null, reps: "4", plates: null },
  { set: 5, multiplier: 0.85, weight: null, reps: "4", plates: null },
  { set: 6, multiplier: 0.80, weight: null, reps: "5", plates: null },
  { set: 7, multiplier: 0.75, weight: null, reps: "6", plates: null },
  { set: 8, multiplier: 0.70, weight: null, reps: "7", plates: null },
  { set: 9, multiplier: 0.65, weight: null, reps: "8+", plates: null },
])

var benchpress_day2_sets = ref([
  { set: 1, multiplier: 0.75, weight: null, reps: "5", plates: null },
  { set: 2, multiplier: 0.85, weight: null, reps: "3", plates: null },
  { set: 3, multiplier: 0.95, weight: null, reps: "1+", plates: null },
  { set: 4, multiplier: 0.90, weight: null, reps: "3", plates: null },
  { set: 5, multiplier: 0.85, weight: null, reps: "5", plates: null },
  { set: 6, multiplier: 0.80, weight: null, reps: "3", plates: null },
  { set: 7, multiplier: 0.75, weight: null, reps: "5", plates: null },
  { set: 8, multiplier: 0.70, weight: null, reps: "3", plates: null },
  { set: 9, multiplier: 0.65, weight: null, reps: "5+", plates: null },
])

var ohp_day1_sets = ref([
  { set: 1, multiplier: 0.50, weight: null, reps: "6", plates: null },
  { set: 2, multiplier: 0.60, weight: null, reps: "5", plates: null },
  { set: 3, multiplier: 0.70, weight: null, reps: "3", plates: null },
  { set: 4, multiplier: 0.70, weight: null, reps: "5", plates: null },
  { set: 5, multiplier: 0.70, weight: null, reps: "7", plates: null },
  { set: 6, multiplier: 0.70, weight: null, reps: "4", plates: null },
  { set: 7, multiplier: 0.70, weight: null, reps: "6", plates: null },
  { set: 8, multiplier: 0.70, weight: null, reps: "8", plates: null },
])

var exercises = ref([
  { id: 0, name: "Bench Press", TM: 170, sets: [benchpress_day1_sets, benchpress_day2_sets] },
  { id: 1, name: "Deadlift", TM: 270, sets: [] },
  { id: 2, name: "Over Head Press", TM: 95, sets: [ohp_day1_sets] },
  { id: 3, name: "Row", TM: 180, sets: [row_day1_sets] },
  { id: 4, name: "Squat", TM: 165, sets: [] }
])

exercises.value.forEach((exercise) => {
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
  var exercise = exercises.value[e.target.id]
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
</script>

<template>
  <div class="card">
    <h2 class="big-button" @click="toggle">Training Max (TM) </h2>
    <div class="wrapper" :class="{ closed: !show_tm, open: show_tm }">
      <!-- <div v-if="show_tm"> -->
      <div class="card-content " v-for="exercise in exercises" :key="exercise.id">
        <div>{{ exercise.name }}</div>
        <input type="number" :value="exercise.TM" :id="exercise.id" @change="onChange" @focus="$event.target.select()">
      </div>
      <!-- </div> -->
    </div>
  </div>

    <div class="card-title">Bench Press</div>
  <div class="table-container">
    <div class="row row-heading">
      <div class="cell cell-heading">Weight</div>
      <div class="cell cell-heading">Reps</div>
      <div class="cell cell-heading">Plates</div>
      <div class="cell cell-heading">Done</div>
    </div>
    <div class="row" :class="{ done: set.done }" v-for="set in benchpress_day1_sets" :key="set.set">
      <div class="cell">{{ set.weight }}</div>
      <div class="cell">{{ set.reps }}</div>
      <div class="cell text-align-left"> <span :class="{
        chip_45: plate == 45,
        chip_35: plate == 35,
        chip_25: plate == 25,
        chip_10: plate == 10,
        chip_5: plate == 5,
        chip_2_5: plate == 2.5
      }" v-for="(plate, index) in set.plates" :key="index">{{ plate }}</span></div>
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