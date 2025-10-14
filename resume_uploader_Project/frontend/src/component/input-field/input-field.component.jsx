
const InputField = ( {label, ...otherProps} ) => {
    return (
        <div className="form-input">

            {
            label && <label htmlFor={otherProps.id}>{label}</label>
            }
                <input
                    {...otherProps}
                />
        </div>
    )
}
export default InputField