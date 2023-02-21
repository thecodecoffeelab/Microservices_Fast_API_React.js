import {Wrapper} from "./Wrapper";
import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";

export const Coffee = () => {
    const [coffee, setCoffee] = useState([]);

    useEffect(() => {
        (async () => {
            const response = await fetch('http://localhost:8000/coffee');
            const content = await response.json();
            setCoffee(content);
        })();
    }, []);

    const del = async id => {
        if (window.confirm('Are you sure to delete this record?')) {
            await fetch(`http://localhost:8000/coffee/${id}`, {
                method: 'DELETE'
            });

            setCoffee(coffee.filter(p => p.id !== id));
        }
    }

    return <Wrapper>
        <div className="pt-3 pb-2 mb-3 border-bottom">
            <Link to={`/create`} className="btn btn-sm btn-outline-secondary">Add Flavour</Link>
        </div>

        <div className="table-responsive">
            <table className="table table-striped table-sm">
                <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Flavour Name</th>
                    <th scope="col">Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Actions</th>
                </tr>
                </thead>
                <tbody>
                {Coffee.map(coffee => {
                    return <tr key={coffee.id}>
                        <td>{coffee.id}</td>
                        <td>{coffee.name}</td>
                        <td>{coffee.price}</td>
                        <td>{coffee.quantity}</td>
                        <td>
                            <a href="/" className="btn btn-sm btn-outline-secondary"
                               onClick={e => del(coffee.id)}
                            >
                                Remove
                            </a>
                        </td>
                    </tr>
                })}
                </tbody>
            </table>
        </div>
    </Wrapper>
}