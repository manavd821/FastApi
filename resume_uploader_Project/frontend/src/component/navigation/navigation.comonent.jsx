import { Link,Outlet } from "react-router";
import './navigation.style.css'
const NavigationLayout  = () => {
    return (
        <div>
            <nav className="navigation-bar">
                <Link to='/'>Home</Link>
                <Link to='/form'>Form</Link>
            </nav>
            <div className="content">
                <Outlet /> 
            </div>
        </div>
    )
}
export default NavigationLayout ;