<script setup>
// eslint-disable-next-line
const props = defineProps({
	no_more_right: Boolean,
	no_more_left: Boolean,
	curr_exercise_name: String
})

// eslint-disable-next-line
const emit = defineEmits(['ev_next_exercise', 'ev_prev_exercise'])
</script>

<template>
	<div class="horizontal-scroll__container">
		<div class="horizontal-scroll__button" @click="emit('ev_prev_exercise')" :class="{ hide: no_more_left }"><img
				src="../assets/chevron_left.svg" alt="Previous" class="horizontal-scroll__button__svg">
		</div>
		<div class="horizontal-scroll__item">{{ curr_exercise_name }}</div>
		<div class="horizontal-scroll__button" @click="emit('ev_next_exercise')" :class="{ hide: no_more_right }"><img
				src="../assets/chevron_right.svg" alt="Next" class="horizontal-scroll__button__svg">
		</div>
	</div>
</template>

<style>
/*=============================================
  =            Horizontal Scroll            =
=============================================*/

.horizontal-scroll__container {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 8px 8px;
	/* background-color: var(--primary-accent-col-2); */
	/* border-bottom: 4px solid var(--primary-accent-col-1); */
	margin-top: 32px;
	margin-bottom: 16px;

}

.horizontal-scroll__button {
	align-items: center;
	background: var(--primary-accent-gradient);
	background-size: var(--background-size);
	border-radius: 64px;
	box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
	color: var(--card-bg-color);
	cursor: pointer;
	display: flex;
	height: 64px;
	justify-content: center;
	line-height: 64px;
	margin: 8px;
	max-height: 64px;
	max-width: 64px;
	min-height: 64px;
	min-width: 64px;
	width: 64px;
}

.horizontal-scroll__button__svg {
	width: 60%;
	height: 60%;
}

.horizontal-scroll__item {
	font-size: var(--font-size-md);
	font-weight: 400;
	background: var(--secondary-accent-gradient);
	color: var(--card-bg-color);
	border-radius: 64px;
	height: 64px;
	line-height: 64px;
	padding: 0px 28px;
	box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}
</style>