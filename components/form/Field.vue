<script lang="ts" setup>
    import { StringSchema } from 'yup';
    interface Props {
        label: string
        type: 'text' | 'email' | 'password'
        name: string
        validator: StringSchema<string> | undefined
        initialValue?: string | null
        validateOnChange?: boolean
    }

     const props = withDefaults(defineProps<Props>(), {
        validator: undefined,
        initialValue: null,
        validateOnChange: false
    })

    const validateOnChange = toRef(props, 'validateOnChange')

    const { value, errorMessage, validate } = useField(props.name, props.validator, {
        initialValue: props.initialValue,
        validateOnValueUpdate: validateOnChange.value
    })

    const labelClass = ref('text-zinc-600')
    const inputClass = ref('border-zinc-300')

    async function handleBlur() {
        if (!validateOnChange.value) {
            const { valid } = await validate()
            if (valid) {
                labelClass.value = 'text-green-700'
                inputClass.value = 'border-green-600'
            } else {
                labelClass.value = 'text-red-500'
                inputClass.value = 'border-red-500'
            }
        }
    }
    async function handleInput() {
        if (validateOnChange.value) {
            const { valid } = await validate()
            if (valid) {
                labelClass.value = 'text-green-700'
                inputClass.value = 'border-green-600'
            } else {
                labelClass.value = 'text-red-500'
                inputClass.value = 'border-red-500'
            }
        }
    }
        
</script>

<template>
    <div class="mt-4">
        <label 
        class="text-sm"
        :class="labelClass"
        >{{ props.label }}</label>
        <input 
        v-model="value"
        :type="props.type"
        :name="props.name"
        class="outline-none border rounded-md block w-full h-[45px] text-sm text-zinc-600 pl-4" 
        :class="inputClass"
        @blur="handleBlur"
        @input="handleInput"
        >
        <div v-if="errorMessage" class="text-red-500 text-sm mt-2">
            {{ errorMessage }}
        </div>
    </div>
</template>
