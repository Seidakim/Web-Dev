import { Component, OnInit } from '@angular/core';
import { products } from '../products';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css'],
})
export class CategoriesComponent implements OnInit {
  products = products;
  constructor() {}

  ngOnInit(): void {}
  categorize(rightId: number) {
    for (let product of products) {
      product.currentCategory = rightId;
    }
  }
}
