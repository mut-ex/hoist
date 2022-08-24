<script setup>
// eslint-disable-next-line
const props = defineProps({
	days: Array,
	current_day: Number,
})

// eslint-disable-next-line
const emit = defineEmits(['ev_day_selected'])
</script>

<template>
	<div class="tab__container">
		<div class="tab" v-for="(day, index) in days" :key="index" :class="{ 'tab--selected': index == current_day }"
			@click="emit('ev_day_selected', index)">{{ day.name }}</div>
	</div>
</template>

<style>
.tab__container {
	color: var(--card-bg-color);
	display: flex;
	font-family: "Roboto Condensed", sans-serif;
	justify-content: space-evenly;
	text-align: center;
}

.tab {
	background-color: var(--primary-accent-col-1);
	/* background: var(--primary-accent-gradient); */
	/* background-size: var(--background-size); */
	border-radius: 6px;
	box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
	color: var(--card-bg-color);
	cursor: pointer;
	flex: 1;
	/* display: block; */
	margin: 8px 8px;
	padding: 4px 4px;
	/* transform: translateZ(0); */
	transition: background-color 0.15s ease-in 
}

.tab--selected {
	/* background: var(--secondary-accent-gradient); */
	background-color: var(--secondary-accent-col-1);
	color: var(--card-bg-color);
}

.tab:first-of-type {
	margin-left: 4px;
}

.tab:last-of-type {
	margin-right: 4px;
}
</style>